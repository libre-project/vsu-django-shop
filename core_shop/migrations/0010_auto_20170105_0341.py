# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_shop', '0009_auto_20170105_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/default/no-img.png', upload_to='product/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
