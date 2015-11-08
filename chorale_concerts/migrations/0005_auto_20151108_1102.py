# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorale_concerts', '0004_concert_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='image',
            new_name='poster',
        ),
    ]
