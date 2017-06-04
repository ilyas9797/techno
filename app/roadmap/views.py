from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from roadmap.models import Roadmap
from roadmap.forms import RoadmapCreatingForm

# Create your views here.


class IndexRoadmaps(generic.ListView):
    template_name = 'roadmap_templates/roadmaps_list.html'
    context_object_name = 'roadmaps'

    def get_queryset(self):
        return Roadmap.objects.all()[:]

'''
def create_roadmap(request):
    if request.method == 'POST':
        creating_form = RoadmapCreatingForm(request.POST)
        if creating_form.is_valid():
            roadmap = creating_form.save()
            for task in creating_form.cleaned_data['tasks']:
                roadmap.task_set.add(task)
            roadmap_url = roadmap.get_absolute_url()
            return HttpResponseRedirect(roadmap_url)
    else:
        creating_form = RoadmapCreatingForm()
    return render(request, 'roadmap_templates/create_roadmap.html',
                  {'form': creating_form,
                   'formurl': reverse('roadmap:roadmap-creating')})
'''


class CreateRoadmap(generic.TemplateView):
    template_name = 'roadmap_templates/create_roadmap.html'

    def get(self, request, *args, **kwargs):
        roadmap_form = RoadmapCreatingForm()
        context = {'form': roadmap_form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        roadmap_form = RoadmapCreatingForm(request.POST)
        if roadmap_form.is_valid():
            roadmap = roadmap_form.save()
            tasks = roadmap_form.cleaned_data['tasks']
            for task in tasks:
                roadmap.task_set.add(task)
            return HttpResponseRedirect(reverse('roadmap:roadmap-detail', kwargs={'pk': roadmap.id}))
        context = {'form': roadmap_form}
        return self.render_to_response(context)


@method_decorator(require_GET, name='dispatch')
class RoadmapDetails(generic.DetailView):
    model = Roadmap
    template_name = 'roadmap_templates/roadmap_details.html'
    context_object_name = 'roadmap'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['roadmap'].task_set.all())
        context['task_set'] = context['roadmap'].task_set.all()[:]
        return context


class DeleteRoadmap(generic.DeleteView):
    model = Roadmap
    success_url = reverse_lazy('roadmap:roadmaps-listing')
