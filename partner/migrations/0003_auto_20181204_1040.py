# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-04 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_auto_20181201_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='food_category',
            field=models.CharField(choices=[('ko', 'Korean'), ('jp', 'Japanese'), ('cn', 'Chinese'), ('it', 'Italian')], default='ko', max_length=2),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='메뉴이미지'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='메뉴명'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.PositiveIntegerField(verbose_name='가격'),
        ),
    ]