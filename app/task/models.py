from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db.models import Max, F, ExpressionWrapper

from roadmap.models import Roadmap
from datetime import timedelta
# Create your models here.


def datetime_validate(value):
    if value < timezone.now():
        raise ValidationError('недопустимый срок выполнения')


def is_critical_task(value):
    if value - timezone.now() <= timezone.timedelta(3):
        return True
    else:
        return False


class FreeTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(roadmap=None)


class Task(models.Model):

    READY = 1
    IN_PROGRESS = 0
    STATE = ((READY, 'ready'),
             (IN_PROGRESS, 'in_progress'))

    title = models.CharField(max_length=100)
    estimate = models.DateTimeField(default=timezone.now, validators=[datetime_validate])
    creating_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(choices=STATE,
                                default=IN_PROGRESS,
                                verbose_name='Состояние задачи: ')
    roadmap = models.ForeignKey(Roadmap, blank=True, null=True, on_delete=models.CASCADE)

    objects = models.Manager()
    free_objects = FreeTaskManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task:task-detail', args=(self.id,))

    def get_url(self):
        return reverse('task:task-detail', args=(self.id,))

    def is_critical(self):
        return is_critical_task(self.estimate)


def calc_scores(scores, task):
    today = scores.ready_time.toordinal()
    create_date = task.creating_time.toordinal()
    estimate = task.estimate.toordinal()
    max_estimate = Task.objects.all().aggregate(max_estimate=Max(F('estimate') - F('creating_time'), output_field=models.IntegerField()))
    max_estimate = timedelta(microseconds=max_estimate['max_estimate']).days
    print(today, create_date, estimate, max_estimate, (today - create_date / estimate - create_date) + (estimate - create_date / max_estimate))
    return (today - create_date / estimate - create_date) + (estimate - create_date / max_estimate)


class ScoresManager(models.Manager):
    def create_scores(self, task):
        scores = self.create(task=task)
        scores.scores = calc_scores(scores, task)
        return scores


class Scores(models.Model):
    ready_time = models.DateTimeField(auto_now=True)
    scores = models.IntegerField(null=True, blank=True)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)

    objects = ScoresManager()

