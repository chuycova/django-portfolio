from django.shortcuts import render
from .models import Project

# Create your views here.

projects = Project.objects.all()
def home(request):
    return render(request, 'portfolio/home.html', {'projects':projects})