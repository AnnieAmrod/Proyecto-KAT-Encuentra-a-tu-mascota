# Generated by Django 3.2 on 2023-04-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='especie',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='raza',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]
