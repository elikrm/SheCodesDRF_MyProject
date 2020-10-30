# Generated by Django 3.0.8 on 2020-09-29 09:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20200929_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 9, 59, 6, 119527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 29, 9, 59, 6, 119527, tzinfo=utc)),
        ),
    ]