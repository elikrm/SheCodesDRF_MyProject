# Generated by Django 3.0.8 on 2020-09-29 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200929_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 29, 19, 23, 43, 711946)),
        ),
    ]
