from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.http import require_GET, require_POST

from . import models, forms
# Create your views here.


class IndexRoadmaps(generic.ListView):
    template_name = 'roadmap_templates/roadmaps_list.html'
    context_object_name = 'roadmaps'

    def get_queryset(self):
        return models.Roadmap.objects.all()[:]

@require_GET
def roadmap_detail(request, **kwargs):
    roadmap = get_object_or_404(models.Roadmap, id=kwargs['pk'])
    return render(request, 'roadmap_templates/roadmap_detail.html',
                  {'roadmap': roadmap,
                   'task_set': roadmap.task_set.all()[:]})


def create_roadmap(request):
    if request.method == 'POST':
        creating_form = forms.RoadmapCreatingForm(request.POST)
        if creating_form.is_valid():
            roadmap = creating_form.save()
            for task in creating_form.cleaned_data['tasks']:
                roadmap.task_set.add(task)
            roadmap_url = roadmap.get_url()
            return HttpResponseRedirect(roadmap_url)
    else:
        creating_form = forms.RoadmapCreatingForm()
    return render(request, 'roadmap_templates/create_roadmap.html',
                  {'form': creating_form,
                   'formurl': reverse('roadmap:roadmap-creating')})

@require_POST
def delete(request, **kwargs):
    roadmap = get_object_or_404(models.Roadmap, id=kwargs['pk'])
    roadmap.delete()
    return HttpResponseRedirect(reverse('roadmap:roadmaps-listing'))

def modify_roadmap(request):
    pass
