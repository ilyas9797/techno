from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse
from django.views import generic

from . import forms, models

# Create your views here.


def create_task(request):
    if request.method == 'POST':
        creating_form = forms.TaskCreatingForm(request.POST)
        if creating_form.is_valid():
            task = creating_form.save()
            task_url = task.get_url()
            return HttpResponseRedirect(task_url)
    else:
        creating_form = forms.TaskCreatingForm()
    return render(request, 'task_templates/create_task.html',
                  {'form': creating_form,
                   'formurl': reverse('task:task-creating')})


@require_GET
def detail(request, **kwargs):
    task = get_object_or_404(models.Task, id=kwargs['pk'])

    return render(request, 'task_templates/task_detail.html',
                  {'task': task,
                   'iscritical': task.is_critical()})


def modify(request, **kwargs):
    task = get_object_or_404(models.Task, id=kwargs['pk'])
    if request.method == 'POST':
        modifying_form = forms.TaskModifyForm(request.POST)
        if modifying_form.is_valid():
            task.delete()
            task = modifying_form.save()
            task_url = task.get_url()
            return HttpResponseRedirect(task_url)
    else:
        modifying_form = forms.TaskModifyForm(instance=task)
    return render(request, 'task_templates/modify_task.html',
                  {'form': modifying_form,
                   'modifying_url': task.get_url_for_modify(),
                   'formurl': reverse('task:task-modifying', args=(task.id,)),
                   'formdeleteurl': reverse('task:task-deleting', args=(task.id,))})

@require_POST
def delete(request, **kwargs):
    task = get_object_or_404(models.Task, id=kwargs['pk'])
    task.delete()
    return HttpResponseRedirect(reverse('task:tasks-listing'))


class IndexTasks(generic.ListView):
    template_name = 'task_templates/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return models.Task.objects.all()[:]