# Generated by Django 5.0.1 on 2024-01-30 17:53

import dengue.models
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dengue', '0028_alter_barangay_is_seasonal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangay',
            name='ar',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='AR(p)'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='i',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='I(d)'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='ma',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='MA(q)'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='seasonal_ar',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='Seasonal AR(P)'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='seasonal_i',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='Seasonal I(D)'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='seasonal_ma',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='Seasonal MA(Q)'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Note: If you want to use the Map make sure to empty the Longitude and Latitude!', null=True, srid=4326),
        ),
    ]
