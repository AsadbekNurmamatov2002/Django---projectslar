from django.shortcuts import render
from .models import Profil, Darsliklar
# Create your views here.

def Darslik(request):
    darslik=Darsliklar.objects.all()
    profil=Profil.objects.all()
    context={
        'darslik':darslik,
        'profil': profil
    }
    return render(request, 'dars.html', context)