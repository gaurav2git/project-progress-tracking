from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Project, Questionaire
from .forms import ProjectForm, QuestionaireForm

# Create your views here.

@login_required
def index(request):
    """View for home/index page"""
    if request.method != "POST":
        projects = Project.objects.order_by('-date_Added')
    else:
        print(request.POST.get('submit'))
        projects = Project.objects.order_by(request.POST.get('submit') + 'date_Added')
    
    count=0
    for project in projects:
        if project.project_Closure:
            count+=1

    content = {
            'projects':projects,
            'page_name':'Dashboard',
            'd_active':'active',
            'count':count,
        }
    return render(request, 'dashboard.html', content)

@login_required
def project_settings(request):
    projects = Project.objects.order_by('-date_Added')
    count=0
    for project in projects:
        if project.project_Closure:
            count+=1

    content = {
            'projects':projects,
            'page_name':'Project Settings',
            'ps_active':'active',
            'count':count,
        }

    return render(request, "project_settings.html", content)

@login_required
def add_project(request):
    if request.method != 'POST':
        form = ProjectForm()
    else:
        form = ProjectForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects:project_settings'))

    content = {'form':form}
    return render(request, 'add_project.html', content)

@login_required
def project_update(request, project_id):
    project = Project.objects.get(id=project_id)
    
    if request.method != 'POST':
        form = ProjectForm(instance=project)
    else:
        form = ProjectForm(instance=project, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects:project_settings'))

    content = {'project':project, 'form':form}
    return render(request, 'project_update.html', content)

@login_required
def view_questionaire(request, project_id):
    project = Project.objects.get(id=project_id)
    questions = Questionaire.objects.filter(related_Project=project)
    count = len(questions)

    content = {
            'project':project,
            'questions':questions,
            'page_name':'Project Settings',
            'ps_active':'active',
            'count':count,
        }

    return render(request, "view_questionaire.html", content)

@login_required
def add_question(request, project_id):
    
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = QuestionaireForm()
    else:
        form = QuestionaireForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects:view_questionaire',args=(project_id,)))

    content = {
            'form':form,
            'project':project,
        }

    return render(request, 'add_question.html', content)

@login_required
def question_update(request, question_id):
    
    question = Questionaire.objects.get(id=question_id)
    
    if request.method != 'POST':
        form = QuestionaireForm(instance=question)
    else:
        form = QuestionaireForm(instance=question, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects:view_questionaire',args=(question.related_Project.id,)))

    content = {'question':question, 'form':form}
    return render(request, 'question_update.html', content)

@login_required
def delete_question(request, question_id):
    question = Questionaire.objects.get(id=question_id)
    print(question_id)
    project_id = question.related_Project.id
    question.delete()
    return HttpResponseRedirect(reverse('projects:view_questionaire',args=(project_id,)))