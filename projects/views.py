from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, Http404
from django.urls import reverse

from users.models import Employee_Profile
from .models import Project, ProjectMember, Questionaire
from .forms import ProjectForm, QuestionaireForm, ProjectMemberForm

import copy

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
    projects = Project.objects.filter(project_Owner=request.user.employee_profile_set.all()[0]).order_by('-date_Added')
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

    content = {
            'form':form,
            'page_name':'Project Settings',
            'ps_active':'active',
        }
    return render(request, 'add_project.html', content)

@login_required
def project_update(request, project_id):
    project = Project.objects.get(id=project_id)
    
    if project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404
    
    warning_message = ""

    if request.method != 'POST':
        form = ProjectForm(instance=project)
    else:
        form = ProjectForm(instance=project, data=request.POST)
        print(form)
        if form.is_valid():
            temp_instance = form.save(commit=False)
            project_members = ProjectMember.objects.filter(project=project)
            if temp_instance.project_Members_Allowed < len(project_members):
                warning_message = "Action Denied!!"
            else:
                form.save()
                return HttpResponseRedirect(reverse('projects:project_settings'))

    content = {
            'project':project,
            'form':form,
            'page_name':'Project Settings',
            'ps_active':'active',
            'warning_message':warning_message,
        }
    return render(request, 'project_update.html', content)

@login_required
def view_questionaire(request, project_id):
    project = Project.objects.get(id=project_id)

    if project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404

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

    if project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404

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
            'page_name':'Project Settings',
            'ps_active':'active',
        }

    return render(request, 'add_question.html', content)

@login_required
def question_update(request, question_id):
    
    question = Questionaire.objects.get(id=question_id)
    
    if question.related_Project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404

    if request.method != 'POST':
        form = QuestionaireForm(instance=question)
    else:
        form = QuestionaireForm(instance=question, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects:view_questionaire',args=(question.related_Project.id,)))

    content = {
            'question':question,
            'form':form,
            'page_name':'Project Settings',
            'ps_active':'active',
        }
    return render(request, 'question_update.html', content)

@login_required
def delete_question(request, question_id):
    question = Questionaire.objects.get(id=question_id)

    if question.related_Project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404

    print(question_id)
    project_id = question.related_Project.id
    question.delete()
    return HttpResponseRedirect(reverse('projects:view_questionaire',args=(project_id,)))

@login_required
def view_team(request, project_id):
    project = Project.objects.get(id=project_id)

    if project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404

    project_members = ProjectMember.objects.filter(project=project)
    count = len(project_members)

    content = {
            'project':project,
            'project_members':project_members,
            'page_name':'Project Settings',
            'ps_active':'active',
            'count':count,
        }

    return render(request, "view_team.html", content)

@login_required
def add_project_member(request, project_id):
    project = Project.objects.get(id=project_id)

    if project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404
    
    project_members = ProjectMember.objects.filter(project=project)
    count = len(project_members)
    
    warning_message = False
    form = False

    if project.project_Members_Allowed == count:
        warning_message = "Project Members Limit Reached"

    else:
        if request.method != 'POST':
            form = ProjectMemberForm()
        else:
            form = ProjectMemberForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('projects:view_team',args=(project_id,)))

    members_got = list(Employee_Profile.objects.filter(is_lead=False))
    members = copy.deepcopy(members_got)
    print(members)
    for member in members_got:
        if len(project_members) >= 0:
            for project_member in project_members:
                print("Project Member",project_member)
                if member == project_member.member:
                    print("Yes")
                    members.remove(member)
    print(members)
    content = {
            'form':form,
            'project':project,
            'members':members,
            'warning_message':warning_message,
            'page_name':'Project Settings',
            'ps_active':'active',
        }

    return render(request, 'add_project_member.html', content)

@login_required
def delete_project_member(request, project_member_id):
    project_member = ProjectMember.objects.get(id=project_member_id)

    if project_member.project.project_Owner != request.user.employee_profile_set.all()[0]:
        raise Http404

    print(project_member_id)
    project_id = project_member.project.id
    project_member.delete()
    return HttpResponseRedirect(reverse('projects:view_team',args=(project_id,)))