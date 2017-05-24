from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'task'

urlpatterns = [
    url(r'^$', views.IndexTasks.as_view(), name='tasks-listing'),
    url(r'^create/$', views.create_task, name='task-creating'),
    url(r'^(?P<pk>[0-9]+)/', include([
        url(r'^$', views.detail, name='task-detail'),
        url(r'^modify/$', views.modify, name='task-modifying'),
        url(r'^delete/$', views.delete, name='task-deleting')
    ]))
]