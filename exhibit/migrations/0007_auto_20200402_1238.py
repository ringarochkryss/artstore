# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-02 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0006_auto_20200402_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryartist',
            old_name='image',
            new_name='artistimage',
        ),
    ]
