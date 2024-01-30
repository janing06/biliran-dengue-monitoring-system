# Generated by Django 4.2 on 2023-10-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dengue', '0026_barangay_is_auto_arima'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangay',
            name='is_auto_arima',
            field=models.BooleanField(default=True, help_text='Checking this will use Auto ARIMA and ignore all the inputs below', verbose_name='Use Auto ARIMA'),
        ),
        migrations.AlterField(
            model_name='barangay',
            name='is_seasonal',
            field=models.BooleanField(default=False, help_text='Checking this will use the Seasonal Component of SARIMA', verbose_name='Use Seasonal ARIMA'),
        ),
    ]