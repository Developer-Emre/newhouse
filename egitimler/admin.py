from django.contrib import admin
from .models import *

class EgitimAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'baslama_tarihi', 'sube', 'hizmet']
    list_filter = ['hizmet', 'sube']
    date_hierarchy = 'baslama_tarihi'
    readonly_fields = ['slug', 'id', 'updated_at']
    search_fields = ['baslik', 'hizmet__isim', 'sube__isim']
    list_per_page = 10


admin.site.register(Egitim, EgitimAdmin)
