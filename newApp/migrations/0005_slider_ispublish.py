# Generated by Django 4.2 on 2023-05-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0004_hakkimizda_alter_hizmet_aciklama_alter_misyon_icerik_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='isPublish',
            field=models.BooleanField(default=False),
        ),
    ]
