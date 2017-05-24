from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'roadmap'

urlpatterns = [
    url(r'^$', views.IndexRoadmaps.as_view(), name='roadmaps-listing'),
    url(r'^create/$', views.create_roadmap, name='roadmap-creating'),
    url(r'^(?P<pk>[0-9]+)/', include([
        url(r'^$', views.roadmap_detail, name='roadmap-detail'),
        url(r'^$', views.modify_roadmap, name='roadmap-modifying'),
        url(r'^delete/$', views.delete, name='roadmap-deleting')
    ]))
]