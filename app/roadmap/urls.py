from django.conf.urls import url, include
from . import views

app_name = 'roadmap'

urlpatterns = [
    url(r'^$', views.IndexRoadmaps.as_view(), name='roadmaps-listing'),
    url(r'^create/$', views.CreateRoadmap.as_view(), name='roadmap-creating'),
    url(r'^(?P<pk>[0-9]+)/', include([
        url(r'^$', views.RoadmapDetails.as_view(), name='roadmap-detail'),
        url(r'^delete/$', views.DeleteRoadmap.as_view(), name='roadmap-deleting')
    ]))
]