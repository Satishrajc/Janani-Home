# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_need', '0005_educationalneed_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalneed',
            name='date_uuid',
            field=models.CharField(blank=True, editable=False, max_length=14, null=True),
        ),
    ]
