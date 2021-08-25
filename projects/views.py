from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id' : '1',
        'title' : 'Data Analysis Pipeline',
        'description':'Exploring, cleaning dataset for ML Model'
    },

    {
        'id' : '2',
        'title' : 'Dynamic Website',
        'description': 'Content Sharing Website'
    
    },

    {
        'id': '3',
        'title' : 'Social Media for Developers',
        'description' : 'Sharing Code and contents'
    }
]



def projects(request):
    page = 'Projects'
    number = 1
    context = {'page': page, 'number' : number, 'projects' : projectList}
    return render(request, 'projects/projects.html', context)

def project(request):
    return render(request, 'projects/single_project.html')