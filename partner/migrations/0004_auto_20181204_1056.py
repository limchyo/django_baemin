# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-04 01:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_auto_20181204_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='food_category',
            new_name='category',
        ),
    ]
