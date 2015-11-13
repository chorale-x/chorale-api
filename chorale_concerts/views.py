from datetime import datetime
import re

from django.shortcuts import get_object_or_404
from django.utils import text

from rest_framework import viewsets, decorators
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from chorale_concerts.models import Concert, Musician, Soloist, Piece, Reservation
from chorale_concerts.serializers import ConcertSerializer, ConcertPosterSerializer, PieceSerializer, SoloistSerializer, MusicianSerializer, ReservationSerializer


class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    filter_fields = ('published', 'booking', )

    @decorators.list_route(methods=['GET'])
    def next(self, request):
        now = datetime.now()
        qs = Concert.objects.filter(date__gte=now, published=True, announced=True).order_by('date')[0:1]
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, 200)

    @decorators.detail_route(methods=['POST'])
    @decorators.parser_classes((MultiPartParser, ))
    def poster(self, request, pk=None):
        concert = get_object_or_404(Concert.objects.all(), pk=pk)

        serializer = ConcertPosterSerializer(data=request.data)
        if serializer.is_valid():
            if concert.poster:
                concert.poster.delete()

            concert.poster = serializer.validated_data.get('poster')
            concert.save()

            return Response(ConcertSerializer(concert).data, 200)
        else:
            return Response(serializer.errors, 400)

    @decorators.detail_route(methods=['put'])
    def remove_poster(self, request, pk=None):
        concert = get_object_or_404(Concert.objects.all(), pk=pk)
        concert.poster.delete()
        serializer = ConcertSerializer(concert)
        return Response(serializer.data, 200)


class PieceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer


class SoloistViewSet(viewsets.ModelViewSet):
    queryset = Soloist.objects.all()
    serializer_class = SoloistSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_fields = ('concert', 'checked', )

    @decorators.list_route(methods=['delete'])
    def empty_concert(self, request):
        concert_id = request.query_params.get('concert', None)
        if concert_id is not None:
            concert = get_object_or_404(Concert.objects.all(), pk=concert_id)
            Reservation.objects.filter(concert=concert).delete()
            return Response(status=204)
        else:
            return Response("No concert specified", 400)
