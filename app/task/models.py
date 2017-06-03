from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.


def datetime_validate(value):
    if value < timezone.now():
        raise ValidationError('недопустимый срок выполнения')


def is_critical_task(value):
    if value - timezone.now() <= timezone.timedelta(3):
        return True
    else:
        return False


class Task(models.Model):
    READY = 1
    IN_PROGRESS = 0
    STATE = ((READY, 'ready'),
             (IN_PROGRESS, 'in_progress'))

    title = models.CharField(max_length=100)
    estimate = models.DateTimeField(default=timezone.now, validators=[datetime_validate])
    creating_time = models.DateTimeField(auto_now=True)
    state = models.IntegerField(choices=STATE,
                                default=IN_PROGRESS,
                                verbose_name='Состояние задачи: ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task:task-detail', args=(self.id,))

    def is_critical(self):
        return is_critical_task(self.estimate)


'''
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
    title = models.CharField(max_length=100)
    estimate = models.DateTimeField(default=timezone.now, validators=[datetime_validate])
    date_time_of_creating = models.DateTimeField(auto_now=True)
    # False="in_progress" True="ready"
    state = models.BooleanField(default=True, verbose_name='Завершено?')
    roadmap = models.ForeignKey(Roadmap, blank=True, null=True, on_delete=models.CASCADE)

    objects = models.Manager()
    free_objects = FreeTaskManager()

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('task:task-detail', args=(self.id,))

    def get_url_for_modify(self):
        return reverse('task:task-modifying', args=(self.id,))

    def is_critical(self):
        return is_critical_task(self.estimate)
'''
