# Generated by Django 4.2 on 2023-08-27 11:02

import dengue.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dengue', '0022_barangay_seasonal_cycle_alter_barangay_seasonal_ar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangay',
            name='is_seasonal',
            field=models.BooleanField(default=False, verbose_name='Seasonality'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='seasonal_ar',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='Seasonal AR'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='seasonal_cycle',
            field=models.IntegerField(choices=[(7, 7), (52, 52)], verbose_name='Seasonal Cycle'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='seasonal_i',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='Seasonal I'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='seasonal_ma',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0), dengue.models.validate_single_digit], verbose_name='Seasonal MA'),
        ),
    ]
