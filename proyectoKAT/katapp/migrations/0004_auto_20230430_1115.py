# Generated by Django 3.2 on 2023-04-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katapp', '0003_auto_20230429_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mfind',
            options={'verbose_name': 'Mascota encontrada', 'verbose_name_plural': 'Mascotas encontradas'},
        ),
        migrations.AlterModelOptions(
            name='mlost',
            options={'verbose_name': 'Mascota Perdida', 'verbose_name_plural': 'Mascotas Perdidas'},
        ),
        migrations.AlterField(
            model_name='mfind',
            name='foto',
            field=models.ImageField(max_length=80, upload_to='', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='mlost',
            name='foto',
            field=models.ImageField(max_length=80, upload_to='', verbose_name='Foto'),
        ),
    ]
