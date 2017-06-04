from django import forms
from . import models
from task.models import Task


class RoadmapCreatingForm(forms.ModelForm):
    class Meta:
        model = models.Roadmap
        fields = ['title']

    tasks = forms.ModelMultipleChoiceField(queryset=Task.objects.filter(roadmap=None).all())