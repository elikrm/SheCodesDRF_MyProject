# Generated by Django 3.0.8 on 2020-09-26 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default='2020-03-20T14:28:23.382748Z'),
        ),
    ]
