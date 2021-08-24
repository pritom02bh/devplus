from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    page = 'Projects'
    return render(request, 'projects/projects.html', {'page':page})

def project(request):
    return render(request, 'projects/single_project.html')