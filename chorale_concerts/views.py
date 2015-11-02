from datetime import datetime

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from chorale_concerts.models import Concert, Musician, Soloist, Piece, Reservation
from chorale_concerts.serializers import ConcertSerializer, PieceSerializer, SoloistSerializer, MusicianSerializer, ReservationSerializer


class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

    @decorators.list_route(methods=['GET'])
    def next(self, request):
        now = datetime.now()
        qs = Concert.objects.filter(date__gte=now, published=True, announced=True).order_by('date')[0:1]
        serializer = self.serializer_class(qs, many=True)
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

