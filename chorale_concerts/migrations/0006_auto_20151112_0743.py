# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorale_concerts', '0005_auto_20151108_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='poster',
            field=models.ImageField(max_length=254, blank=True, upload_to='posters'),
        ),
    ]
