# Generated by Django 3.2 on 2023-05-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_color_codigo_hexadecimal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='codigo_hexadecimal',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Código hexadecimal del color'),
        ),
    ]
