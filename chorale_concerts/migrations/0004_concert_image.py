# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorale_concerts', '0003_auto_20151107_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='image',
            field=models.ImageField(max_length=254, upload_to=b'posters', blank=True),
        ),
    ]
