# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 09:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 19, 9, 30, 22, 516883, tzinfo=utc)),
        ),
    ]
