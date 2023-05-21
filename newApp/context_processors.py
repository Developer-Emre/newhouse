from .models import *
from egitimler.models import *

def check_all(request):
    egitimler = Egitim.objects.filter(isPublish = True)
    karisik = []
    egitimTurListesi = [] 
    for egitim in egitimler:
        if egitim.hizmet not in egitimTurListesi: 
            karisik.append(egitim) 
            egitimTurListesi.append(egitim.hizmet)
    hakkimizda =  Hakkimizda.objects.all()[:1]
    slogan = Slogan.objects.all()[:1]
    hizmetler = Hizmet.objects.all()
    misyon = Misyon.objects.all()[:1]
    vizyon = Vizyon.objects.all()[:1]
    slider = Slider.objects.filter(isPublish = True)
    programlar = Program.objects.all()
    hizmetlerimiz = Hizmetler.objects.all()[:1]
    galeri = Galeri.objects.all()


    context = {
        'egitimler':egitimler,
        'hakkimizda':hakkimizda,
        'slogan':slogan,
        'hizmetler':hizmetler,
        'misyon':misyon,
        'vizyon':vizyon,
        'slider':slider,
        'programlar':programlar,
        'karisik':karisik,
        'hizmetlerimiz':hizmetlerimiz,
        'galeri':galeri,
    }
    return context
