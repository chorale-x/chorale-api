from rest_framework import serializers

from chorale_concerts.models import Concert, Piece, Soloist, Musician, Reservation


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        extra_kwargs = {'concert': {'write_only': True}}

    concert_id = serializers.PrimaryKeyRelatedField(read_only=True)


class SoloistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soloist
        extra_kwargs = {'concert': {'write_only': True}}

    concert_id = serializers.PrimaryKeyRelatedField(read_only=True)


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        extra_kwargs = {'concert': {'write_only': True}}

    concert_id = serializers.PrimaryKeyRelatedField(read_only=True)


class ConcertSerializer(serializers.ModelSerializer):
    pieces = PieceSerializer(many=True, read_only=True)
    soloists = SoloistSerializer(many=True, read_only=True)
    musicians = MusicianSerializer(many=True, read_only=True)
    class Meta:
        model = Concert
        read_only_fields = ('poster', )


class ConcertPosterSerializer(serializers.Serializer):
    poster = serializers.ImageField(max_length=254)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        extra_kwargs = {'concert': {'write_only': True}}

    concert_id = serializers.PrimaryKeyRelatedField(read_only=True)
