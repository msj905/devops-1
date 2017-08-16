# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-12 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20170812_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(1, '在线'), (3, '故障'), (2, '已下线'), (4, '备用')], default=1, null=True, verbose_name='资产状态'),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(1, '在线'), (3, '故障'), (2, '已下线'), (4, '备用')], default=0, verbose_name='资产状态'),
        ),
    ]
