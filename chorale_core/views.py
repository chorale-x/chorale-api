import requests, json

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from rest_framework import viewsets, decorators
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from chorale_core.models import UserSerializer, Comment, CommentSerializer, SubscriberSerializer


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


class SubscriberList(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        url = 'https://us10.api.mailchimp.com/3.0/lists/' + LIST_ID + '/members?offset=0&count=10000'
        headers = {'Content-type': 'application/json', 'Authorization': 'apikey ' + API_KEY}
        r = requests.get(url, headers=headers)
        members = []
        for m in r.json()['members']:
            mem = {
                'id': m['id'],
                'email_address': m['email_address'],
                'status': m['status'],
                'civility': m['merge_fields']['CIVILITY'],
                'first_name': m['merge_fields']['LNAME'],
                'last_name': m['merge_fields']['FNAME'],
                'phone': m['merge_fields']['PHONE']
            }
            members.append(mem)

        serializer = SubscriberSerializer(members, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            payload = {
                'email_address': serializer.data.get('email_address'),
                'status': 'pending',
                'merge_fields': {
                    'CIVILITY': serializer.data.get('civility'),
                    'LNAME': serializer.data.get('last_name'),
                    'FNAME': serializer.data.get('first_name'),
                    'PHONE': serializer.data.get('phone')
                }
            }
            json_payload = json.dumps(payload)
            url = 'https://us10.api.mailchimp.com/3.0/lists/' + LIST_ID + '/members'
            headers = {'Content-type': 'application/json', 'Content-Length': len(json_payload), 'Authorization': 'apikey ' + API_KEY}
            r = requests.post(url, headers=headers, data=json_payload)

            m = r.json()
            mem = {
                'id': m['id'],
                'email_address': m['email_address'],
                'status': m['status'],
                'civility': m['merge_fields']['CIVILITY'],
                'first_name': m['merge_fields']['LNAME'],
                'last_name': m['merge_fields']['FNAME'],
                'phone': m['merge_fields']['PHONE']
            }
            rep_serial = SubscriberSerializer(mem)
            return Response(rep_serial.data, 200)
        else:
            return Response(serializer.errors, 400)


class SubscriberDetail(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk=None):
        url = 'https://us10.api.mailchimp.com/3.0/lists/' + LIST_ID + '/members/' + pk
        headers = {'Content-type': 'application/json', 'Authorization': 'apikey ' + API_KEY}
        r = requests.get(url, headers=headers)

        if r.status_code == 404:
            return Response("Resource not found", 404)

        m = r.json()
        mem = {
            'id': m['id'],
            'email_address': m['email_address'],
            'status': m['status'],
            'civility': m['merge_fields']['CIVILITY'],
            'first_name': m['merge_fields']['LNAME'],
            'last_name': m['merge_fields']['FNAME'],
            'phone': m['merge_fields']['PHONE']
        }
        serializer = SubscriberSerializer(mem)
        return Response(serializer.data, 200)

    def delete(self, request, pk=None):
        url = 'https://us10.api.mailchimp.com/3.0/lists/' + LIST_ID + '/members/' + pk
        headers = {'Content-type': 'application/json', 'Authorization': 'apikey ' + API_KEY}
        r = requests.delete(url, headers=headers)

        if r.status_code == 204:
            return Response(status=204)
        else:
            return Response(r.json(), r.status_code)
