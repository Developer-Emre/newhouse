from django.shortcuts import render, redirect
from .models import *
from egitimler.models import *

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def galeri(request):
    
    return render(request,'galeri.html')

def misyonVizyon(request):
    
    return render(request,'mission-vission.html')

def Programlar(request):
    
    return render(request,'programlar.html')

def Register(request):

    return render(request,'programlar.html')

def egitimler(request, slug):
    egitimler = Egitim.objects.filter(hizmet__slug = slug, isPublish = True)
    hizmet = Hizmet.objects.get(slug = slug)
    context = {
        'egitimler':egitimler,
        'hizmetimiz':hizmet
    }
    return render(request, 'egitimler.html', context)


def hakkimizda(request):
    return render(request,'hakkimizda.html')

def view_404(request, exception):
    return redirect('/')

def view_500(request):
    return render(request, 'hata.html')