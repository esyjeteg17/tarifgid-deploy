# Generated by Django 5.0.6 on 2024-07-13 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0007_region_tariff_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Регионы', 'verbose_name_plural': 'Регионы'},
        ),
    ]
