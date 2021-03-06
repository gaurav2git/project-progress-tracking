from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('projects:index'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('projects:index'))

    content = {'form':form}
    return render(request, 'register.html', content)

@login_required
def profile(request):
    emp_profile = Employee_Profile.objects.filter(related_user = request.user)

    content = {
            'emp_profile':emp_profile,
            'page_name':'Profile',
            'p_active':'active'
        }
    return render(request, 'profile.html', content)
