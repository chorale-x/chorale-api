# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorale_concerts', '0002_auto_20151017_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='firstname',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='soloist',
            name='firstname',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
