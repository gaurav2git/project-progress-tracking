from django.shortcuts import render

from .models import Project

# Create your views here.
def index(request):
    """View for home/index page"""
    projects = Project.objects.order_by('date_added')
    content = {'projects':projects}
    return render(request, 'index.html', content)