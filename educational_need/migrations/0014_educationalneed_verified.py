# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-03 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_need', '0013_educationalneed_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalneed',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]