# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geopage', '0003_bookpagerelatedlinks_geolocation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookPageRelatedLinks',
            new_name='GeoPageRelatedLocations',
        ),
    ]