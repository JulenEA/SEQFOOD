# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('c2dna', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('origen', models.CharField(max_length=70)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]
