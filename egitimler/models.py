from django.db import models
from newApp.models import *
import uuid
# Create your models here.
class Egitim(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hizmet = models.ForeignKey(Hizmet, on_delete = models.CASCADE)
    baslik = models.CharField(max_length = 100)
    aciklama = models.TextField(blank=True)
    resim = models.ImageField(upload_to = 'egitim_resimleri', verbose_name='Eğitim Resmi')
    baslama_tarihi = models.DateField()
    sure = models.CharField(max_length=100)
    fiyat = models.IntegerField()
    sube = models.ForeignKey(Sube, on_delete = models.CASCADE)
    slug = models.SlugField(max_length=100, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isPublish = models.BooleanField(default=False, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.baslik + '-' + str(self.id)[:5])
        super(Egitim, self).save(*args, **kwargs)
    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = 'Eğitim'
        verbose_name_plural = 'Eğitimler'
        ordering = ['-created_at']
