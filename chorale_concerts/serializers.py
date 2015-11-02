from rest_framework import serializers

from chorale_concerts.models import Concert, Piece, Soloist, Musician, Reservation


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece


class SoloistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soloist


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician


class ConcertSerializer(serializers.ModelSerializer):
    pieces = PieceSerializer(many=True, read_only=True)
    soloists = SoloistSerializer(many=True, read_only=True)
    musicians = MusicianSerializer(many=True, read_only=True)
    class Meta:
        model = Concert


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation

