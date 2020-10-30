# Generated by Django 3.0.8 on 2020-09-29 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200926_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 29, 19, 19, 53, 685392)),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]