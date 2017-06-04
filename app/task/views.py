from django.views.decorators.http import require_GET
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
