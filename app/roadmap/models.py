from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.


class Roadmap(models.Model):
    title = models.CharField(max_length=100)
    date_time_of_creating = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('roadmap:roadmap-detail', args=(self.id,))

