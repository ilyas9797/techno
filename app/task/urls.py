from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'task'

urlpatterns = [
    url(r'^$', views.IndexTasks.as_view(), name='tasks-listing'),
    url(r'^create/$', views.CreateTask.as_view(), name='task-creating'),
    url(r'^(?P<pk>[0-9]+)/', include([
        url(r'^$', views.TaskDetails.as_view(), name='task-detail'),
        url(r'^modify/$', views.ModifyTask.as_view(), name='task-modifying'),
        url(r'^delete/$', views.DeleteTask.as_view(), name='task-deleting')
    ]))
]