from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator

from task.models import Task

# Create your views here.


class IndexTasks(generic.ListView):
    template_name = 'task_templates/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()[:]


class CreateTask(generic.CreateView):
    model = Task
    template_name = 'task_templates/create_task.html'
    fields = ['title', 'estimate']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_url'] = reverse('task:task-creating')
        return context


@method_decorator(require_GET, name='dispatch')
class TaskDetails(generic.DetailView):
    model = Task
    template_name = 'task_templates/task_details.html'
    context_object_name = 'task'


class ModifyTask(generic.UpdateView):
    model = Task
    template_name = 'task_templates/modify_task.html'
    fields = ['title', 'estimate', 'state']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_url'] = reverse('task:task-modifying', kwargs={'pk': context['task'].id})
        context['form_delete_url'] = reverse('task:task-deleting', kwargs={'pk': context['task'].id})
        return context


class DeleteTask(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('task:tasks-listing')

'''
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
        modifying_form = forms.TaskModifyForm(request.POST, instance=task)
        if modifying_form.is_valid():
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
'''
