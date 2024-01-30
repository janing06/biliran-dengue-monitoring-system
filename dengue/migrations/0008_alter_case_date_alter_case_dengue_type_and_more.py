# Generated by Django 4.2 on 2023-05-26 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dengue', '0007_alter_resident_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='case',
            name='dengue_type',
            field=models.CharField(choices=[('DENV1', 'DENV1'), ('DENV2', 'DENV2'), ('DENV3', 'DENV3'), ('DENV4', 'DENV4')], max_length=5, verbose_name='Dengue Type'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='barangay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dengue.barangay', verbose_name='Barangay'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='municipal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dengue.municipal', verbose_name='Municipal'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='resident_id',
            field=models.CharField(max_length=11, unique=True, verbose_name='Residence ID'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, verbose_name='Sex'),
        ),
    ]