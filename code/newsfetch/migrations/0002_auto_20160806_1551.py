# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfetch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='content_snippet',
            field=models.CharField(max_length=1000),
        ),
    ]
