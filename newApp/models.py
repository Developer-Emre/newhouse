from django.db import models
import uuid
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Hizmetler(models.Model):
    baslik = models.CharField(max_length=100)
    aciklama = RichTextField(verbose_name="Açıklama", blank=True)

    def __str__(self):
        return self.baslik
    
    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetlerimiz Anasayfa"
class Hizmet(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = RichTextField(verbose_name="Açıklama (Opsiyonel)", blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, editable=False)
    def __str__(self):
        return self.isim
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim.replace("/", "-").replace('ı', 'i'))
        super(Hizmet, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"

class Hakkimizda(models.Model):
    baslik = models.CharField(max_length=100)
    ozet = RichTextField(verbose_name="Özet (Anasayfada Çıkacak Olan Kısım)", blank=True, null=True)
    icerik = RichTextField()
    resim = models.ImageField(upload_to="hakkimizda/", blank=True, null=True)

    def __str__(self):
        return self.baslik

class Sube(models.Model):
    isim = models.CharField(max_length=100)
    resim = models.ImageField(upload_to="sube/", blank=True, null=True, verbose_name='Şube Resmi (Opsiyonel)')

    def __str__(self):
        return self.isim

class Slogan(models.Model):
    baslik = models.CharField(max_length=100)
    slogan = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.baslik

class Misyon(models.Model):
    slogan = models.ForeignKey(Slogan, on_delete=models.SET_NULL, null=True, blank=True)
    baslik = models.CharField(max_length=100)
    icerik = RichTextField()
    resim = models.ImageField(upload_to="misyon/", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = slugify(self.baslik)
        super(Misyon, self).save(*args, **kwargs)

class Vizyon(models.Model):
    slogan = models.ForeignKey(Slogan, on_delete=models.SET_NULL, null=True, blank=True)
    isim = models.CharField(max_length=100)
    icerik = RichTextField()
    resim = models.ImageField(upload_to="vizyon/", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.isim
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super(Vizyon, self).save(*args, **kwargs)
    

class Slider(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = RichTextField(verbose_name="Açıklama (Opsiyonel)", blank=True, null=True)
    resim = models.ImageField(upload_to="slider/", blank=True, null=True)
    sira = models.IntegerField(default=0)
    isPublish = models.BooleanField(default=False)

    def __str__(self):
        return self.isim
    
    class Meta:
        ordering = ["sira"]
        verbose_name = "Slider"
        verbose_name_plural = "Slider"

class Galeri(models.Model):
    isim = models.CharField(max_length=100)
    resim = models.ImageField(upload_to="galeri/", blank=True, null=True)
    sira = models.IntegerField(default=0)
    aciklama = RichTextField(verbose_name="Açıklama", blank=True, null=True)

    def __str__(self):
        return self.isim
    
    class Meta:
        ordering = ["sira"]
        verbose_name = "Galeri"
        verbose_name_plural = "Galeri"

class Program(models.Model):
    baslik = models.CharField(max_length=100)
    iframe = models.CharField(max_length=300)
    aciklama = RichTextField(verbose_name="Açıklama", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.baslik
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.baslik)
        super(Program, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programlar"






class GenelVizyon(models.Model):
    icerik = RichTextField()

class GenelProgram(models.Model):
    icerik = RichTextField()

    