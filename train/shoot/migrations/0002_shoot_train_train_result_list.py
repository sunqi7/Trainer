# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-09 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoot_train',
            name='train_result_list',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
