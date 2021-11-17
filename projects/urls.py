from django.urls import path, include
from projects import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/settings', views.project_settings, name='project_settings'),
    path('projects/add_project', views.add_project, name='add_project'),
    path('projects/project_update/<int:project_id>', views.project_update, name='project_update'),
    path('projects/view_questionaire/<int:project_id>', views.view_questionaire, name='view_questionaire'),
    path('projects/add_question/<int:project_id>', views.add_question, name='add_question'),
    path('projects/question_update/<int:question_id>', views.question_update, name='question_update'),
    path('projects/delete_question/<int:question_id>', views.delete_question, name='delete_question'),
    path('projects/view_team/<int:project_id>', views.view_team, name='view_team'),
    path('projects/add_project_member/<int:project_id>', views.add_project_member, name='add_project_member'),
    path('projects/delete_project_member/<int:project_member_id>', views.delete_project_member, name='delete_project_member'),
    path('projects/your_projects', views.your_projects, name='your_projects'),
    path('projects/view_project/<int:project_id>', views.view_project, name='view_project'),
    path('projects/answer/<int:question_id>', views.answer, name='answer'),
    path('projects/view_answers/<int:question_id>', views.view_answers, name='view_answers'),
    path('projects/view_answer/<int:answer_id>', views.view_answer, name='view_answer'),
    path('projects/delete_answer/<int:answer_id>', views.delete_answer, name='delete_answer'),
]