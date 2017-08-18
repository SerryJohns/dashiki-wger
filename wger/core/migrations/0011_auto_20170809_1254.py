# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-09 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170725_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='show_english_ingredients',
            field=models.BooleanField(default=True, help_text='Check to also show ingredients in English while creating\na nutritional plan. These ingredients are extracted from a list provided\nby the US Department of Agriculture. It is extremely complete, with around\n7000 entries, but can be somewhat overwhelming and\nmake the search difficult.', verbose_name='Also use ingredients in English'),
        ),
    ]
