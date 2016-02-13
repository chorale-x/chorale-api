# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorale_concerts', '0006_auto_20151112_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='has_student_places',
            field=models.BooleanField(default=True),
        ),
    ]
