from django.shortcuts import render
from .models import DarsProject, ProjectsModel,ProjectUrta

# Create your views here.
def Home(request):
    projects=ProjectsModel.objects.all()
    project=DarsProject.objects.all()
    urta=ProjectUrta.objects.all()
    context={
        "project":project,
        'projects':projects,
        "urta":urta
    }
    return render(request, 'index.html', context)

def Dars(request, id):
    pro=DarsProject.objects.get(id=id)
    context={
        'pro':pro
    }
    return render(request, 'dars.html', context)