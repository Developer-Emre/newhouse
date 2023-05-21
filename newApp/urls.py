
from django.urls import path
from .views import *
from django.contrib.auth import login


urlpatterns = [
    path('',index,name="index"),
    path('galeri/',galeri,name="galeri"),
    path('misyon/',misyonVizyon,name="misyonvizyon"),
    path('programlar/',Programlar,name="programlar"),
    path('egitimler/<str:slug>',egitimler,name="egitimler"),
    path('hakkimizda/',hakkimizda,name="hakkimizda"),
] 
