# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-01 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0002_auto_20200329_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryart',
            name='techniques',
            field=models.CharField(default='lin', max_length=254),
        ),
        migrations.AlterField(
            model_name='galleryartist',
            name='artistname',
            field=models.CharField(default='Elin', max_length=254),
        ),
        migrations.AlterField(
            model_name='galleryartist',
            name='techniques',
            field=models.CharField(default='Lin', max_length=254),
        ),
    ]
