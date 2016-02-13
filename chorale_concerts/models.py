from django.db import models

from rest_framework import serializers


class Concert(models.Model):
    date = models.DateTimeField()
    place = models.CharField(max_length=254)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    orchestra = models.CharField(max_length=254, blank=True)
    director_lastname = models.CharField(max_length=100, blank=True)
    director_firstname = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters', max_length=254, blank=True)
    published = models.BooleanField(default=True)
    announced = models.BooleanField(default=False)
    booking = models.BooleanField(default=False)
    has_student_seats = models.BooleanField(default=True)
    has_numbered_seats = models.BooleanField(default=True)
    fnac = models.URLField(max_length=254, blank=True)
    eventbrite = models.URLField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return "Concert du {:%d %b %Y}".format(self.date)


class Piece(models.Model):
    title = models.CharField(max_length=254)
    composer_lastname = models.CharField(max_length=100)
    composer_firstname = models.CharField(max_length=100, blank=True)
    concert = models.ForeignKey(Concert, related_name='pieces')
    rank = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return "%s (%s) - %s" % (self.title, self.composer_lastname, self.concert.__str__())


class Soloist(models.Model):
    voice = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100, blank=True)
    concert = models.ForeignKey(Concert, related_name='soloists')
    rank = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return "%s %s (%s) - %s" % (self.lastname, self.firstname, self.voice, self.concert.__str__())


class Musician(models.Model):
    instrument = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100, blank=True)
    concert = models.ForeignKey(Concert, related_name='musicians')
    rank = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return "%s %s (%s) - %s" % (self.lastname, self.firstname, self.instrument, self.concert.__str__())


class Reservation(models.Model):
    civility = models.CharField(max_length=30)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30)
    concert = models.ForeignKey(Concert, related_name='reservations')
    numbered_seats = models.PositiveSmallIntegerField(default=0)
    normal_seats = models.PositiveSmallIntegerField(default=0)
    cheap_seats = models.PositiveSmallIntegerField(default=0)
    reduced_seats = models.PositiveSmallIntegerField(default=0)
    message = models.TextField(blank=True)
    subscriber = models.BooleanField(default=True)
    checked = models.BooleanField(default=False)
