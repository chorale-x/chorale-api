# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorale_concerts', '0007_concert_has_student_places'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='has_student_places',
            new_name='has_student_seats',
        ),
        migrations.AddField(
            model_name='concert',
            name='has_numbered_seats',
            field=models.BooleanField(default=True),
        ),
    ]
