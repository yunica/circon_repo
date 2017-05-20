# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_purchasedetail_total_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedetail',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
