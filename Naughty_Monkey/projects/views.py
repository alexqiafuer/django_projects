from django.shortcuts import render

def projects(request):
    return render(request, 'projects/projects.html')

def project(request):
    return render(request, 'projects/single-project.html')