# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-05 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=100, null=True),
        ),
    ]
