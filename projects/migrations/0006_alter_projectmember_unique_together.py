# Generated by Django 3.2.9 on 2021-11-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0005_projectmember'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='projectmember',
            unique_together={('project', 'member')},
        ),
    ]
