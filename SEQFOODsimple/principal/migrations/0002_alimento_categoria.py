# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='categoria',
            field=models.CharField(choices=[('1', 'carne'), ('2', 'pescado'), ('3', 'lacteo'), ('4', 'fruta'), ('5', 'otra')], default=5, max_length=1),
        ),
    ]
