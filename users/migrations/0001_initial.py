# Generated by Django 3.2.9 on 2021-11-15 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_i_d', models.PositiveIntegerField()),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_email', models.EmailField(max_length=254)),
                ('employee_designation', models.CharField(max_length=100)),
                ('employee_department', models.CharField(max_length=100)),
                ('employee_location', models.CharField(choices=[('BLR1', 'Bangalore One'), ('BLR2', 'Bangalore Two'), ('GUR', 'Gurugram'), ('PUN', 'Pune'), ('KOC', 'Kochi')], max_length=50)),
                ('is_lead', models.BooleanField(default=False)),
                ('related_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
