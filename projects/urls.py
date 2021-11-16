from django.urls import path, include
from projects import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/settings', views.project_settings, name='project_settings'),
    path('projects/add_project', views.add_project, name='add_project'),
    path('projects/project_update/<int:project_id>', views.project_update, name='project_update'),
]