# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profile_liked_recipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('time_in_seconds', models.IntegerField()),
                ('tags', models.TextField(blank=True)),
                ('ingredient_list', models.TextField(blank=True)),
                ('isYummlyRecipe', models.BooleanField(default=False)),
                ('isUserRecipe', models.BooleanField(default=False)),
                ('ingredients', models.ManyToManyField(to='main.Ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='yummlyrecipe',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_recipes',
            field=models.ManyToManyField(to='main.Recipe'),
        ),
        migrations.DeleteModel(
            name='YummlyRecipe',
        ),
    ]
