# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=254)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('orchestra', models.CharField(blank=True, max_length=254)),
                ('director_lastname', models.CharField(blank=True, max_length=100)),
                ('director_firstname', models.CharField(blank=True, max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('published', models.BooleanField(default=True)),
                ('announced', models.BooleanField(default=False)),
                ('booking', models.BooleanField(default=False)),
                ('fnac', models.URLField(blank=True, max_length=254)),
                ('eventbrite', models.URLField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=1)),
                ('concert', models.ForeignKey(related_name='musicians', to='chorale_concerts.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('composer_lastname', models.CharField(max_length=100)),
                ('composer_firstname', models.CharField(blank=True, max_length=100)),
                ('rank', models.IntegerField(default=1)),
                ('concert', models.ForeignKey(related_name='pieces', to='chorale_concerts.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='Soloist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=1)),
                ('concert', models.ForeignKey(related_name='soloists', to='chorale_concerts.Concert')),
            ],
        ),
    ]
