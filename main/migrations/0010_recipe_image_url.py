# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170407_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]