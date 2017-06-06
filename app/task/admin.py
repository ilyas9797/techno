from django.contrib import admin
from .models import Task, Scores

# Register your models here.



admin.site.register((Task, Scores))