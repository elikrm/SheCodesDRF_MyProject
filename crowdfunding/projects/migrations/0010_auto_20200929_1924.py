# Generated by Django 3.0.8 on 2020-09-29 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200929_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 29, 19, 24, 42, 253576)),
        ),
    ]
