# Generated by Django 5.0.6 on 2024-07-13 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0006_rename_isfavotite_tariff_isfavorite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tariff',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tariffs.region'),
        ),
    ]
