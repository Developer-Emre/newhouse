# Generated by Django 4.2 on 2023-05-21 20:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0012_galeri_aciklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenelVizyon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icerik', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
