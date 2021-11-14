from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.

@login_required
def index(request):
    """View for home/index page"""
    projects = Project.objects.order_by('date_added')
    content = {'projects':projects}
    return render(request, 'dashboard.html', content)