# Generated by Django 4.2 on 2023-05-21 19:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0006_hizmet_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='aciklama',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama (Opsiyonel)'),
        ),
    ]
