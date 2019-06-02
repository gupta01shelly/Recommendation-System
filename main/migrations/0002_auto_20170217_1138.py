# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='yummlyrecipe',
            name='ingredient',
            field=models.ManyToManyField(to='main.Ingredient'),
        ),
    ]