from django.contrib import admin

from chorale_concerts.models import Concert, Piece, Soloist, Musician, Reservation

admin.site.register(Concert)
admin.site.register(Piece)
admin.site.register(Soloist)
admin.site.register(Musician)
admin.site.register(Reservation)