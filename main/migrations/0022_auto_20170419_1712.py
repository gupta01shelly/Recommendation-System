# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20170419_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='disliked_recipes',
            field=models.ManyToManyField(blank=True, related_name='profiles_disliked', to='main.Recipe'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_recipes',
            field=models.ManyToManyField(blank=True, related_name='profiles_liked', to='main.Recipe'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='saved_recipes',
            field=models.ManyToManyField(blank=True, related_name='profiles_saved', to='main.Recipe'),
        ),
    ]
