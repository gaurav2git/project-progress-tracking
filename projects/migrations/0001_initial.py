# Generated by Django 3.2.9 on 2021-11-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectCode', models.PositiveIntegerField()),
                ('projectName', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('projectDescription', models.TextField()),
                ('projectMembersAllowed', models.PositiveIntegerField(default=5)),
            ],
        ),
    ]
