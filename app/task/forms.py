from django import forms
from . import models


class TaskCreatingForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'estimate']
        widgets = {'estimate': forms.DateTimeInput}

class TaskModifyForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'

