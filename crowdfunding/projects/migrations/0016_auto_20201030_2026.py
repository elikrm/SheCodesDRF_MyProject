# Generated by Django 3.0.8 on 2020-10-30 10:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20201030_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 10, 26, 8, 909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 10, 26, 8, 909, tzinfo=utc)),
        ),
    ]