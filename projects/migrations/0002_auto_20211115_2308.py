# Generated by Django 3.2.9 on 2021-11-15 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='date_added',
            new_name='date_Added',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='projectCode',
            new_name='project_Code',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='projectDescription',
            new_name='project_Description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='projectMembersAllowed',
            new_name='project_Members_Allowed',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='projectName',
            new_name='project_Name',
        ),
        migrations.AddField(
            model_name='project',
            name='project_Closure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='project_Progress',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]