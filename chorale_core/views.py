from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from rest_framework import viewsets, decorators
from rest_framework.response import Response
from rest_framework.views import APIView

from chorale_core.models import UserSerializer, Comment, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @decorators.list_route()
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GalleryList(APIView):
    def get(self, request):
        fs = FileSystemStorage(location='media/gallery')
        _, photos = fs.listdir('')
        p_list = []
        id = 1
        for p in photos:
            if p != '.DS_Store':
                p_list.append({'id': id, 'href': fs.base_url + 'gallery/' + p, 'thumbnail': fs.base_url + 'gallery/thumbnails/' + p})
                id = id+1

        return Response(p_list, 200)
