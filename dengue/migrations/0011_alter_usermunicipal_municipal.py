# Generated by Django 4.2 on 2023-06-09 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dengue', '0010_usermunicipal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermunicipal',
            name='municipal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dengue.municipal'),
        ),
    ]