# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-29 22:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_comment_rejected_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2017, 7, 29, 22, 10, 40, 301311, tzinfo=utc)),
        ),
    ]
