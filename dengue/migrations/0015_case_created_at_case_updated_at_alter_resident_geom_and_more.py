# Generated by Django 4.2 on 2023-07-01 16:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dengue', '0014_alter_case_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Latitude and Longitude will be prioritize if not empty(Optional)', null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='resident',
            name='street',
            field=models.CharField(blank=True, help_text='(Optional)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='suffix',
            field=models.CharField(blank=True, choices=[('Sr', 'Sr'), ('Jr', 'Jr'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], help_text='(Optional)', max_length=3, null=True),
        ),
    ]
