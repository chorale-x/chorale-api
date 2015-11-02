# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chorale_concerts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('civility', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=30)),
                ('numbered_seats', models.PositiveSmallIntegerField(default=0)),
                ('normal_seats', models.PositiveSmallIntegerField(default=0)),
                ('cheap_seats', models.PositiveSmallIntegerField(default=0)),
                ('reduced_seats', models.PositiveSmallIntegerField(default=0)),
                ('message', models.TextField(blank=True)),
                ('subscriber', models.BooleanField(default=True)),
                ('checked', models.BooleanField(default=False)),
                ('concert', models.ForeignKey(to='chorale_concerts.Concert', related_name='reservations')),
            ],
        ),
        migrations.AlterField(
            model_name='musician',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='piece',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='soloist',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
