from django.contrib import admin
from .models import *
# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ['isim', 'sira']
    list_editable = ['sira']

class GaleriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'sira']
    list_editable = ['sira']

class HizmetAdmin(admin.ModelAdmin):
    list_display = ['isim', 'slug']

    readonly_fields = ['slug']

admin.site.register(Slider, SliderAdmin)
admin.site.register(Galeri, GaleriAdmin)
admin.site.register(Hizmet, HizmetAdmin)
admin.site.register(Vizyon)
admin.site.register(Misyon)
admin.site.register(Program)
admin.site.register(Slogan)
admin.site.register(Hakkimizda)
admin.site.register(Hizmetler)
admin.site.register(Sube)
admin.site.register(GenelVizyon)