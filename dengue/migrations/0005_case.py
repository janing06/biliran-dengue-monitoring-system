# Generated by Django 4.2 on 2023-04-06 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dengue', '0004_resident'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('dengue_type', models.CharField(choices=[('DENV1', 'DENV1'), ('DENV2', 'DENV2'), ('DENV3', 'DENV3'), ('DENV4', 'DENV4')], max_length=5)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resident', to='dengue.resident')),
            ],
        ),
    ]