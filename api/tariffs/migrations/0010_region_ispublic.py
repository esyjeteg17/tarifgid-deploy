# Generated by Django 5.0.6 on 2024-07-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0009_delete_homephonetariff_delete_internettariff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='isPublic',
            field=models.BooleanField(default=False),
        ),
    ]
