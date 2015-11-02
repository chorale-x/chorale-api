"""chorale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from chorale_core.views import UserViewSet, CommentViewSet
from chorale_concerts.views import ConcertViewSet, PieceViewSet, SoloistViewSet, MusicianViewSet, ReservationViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'comment', CommentViewSet)

router.register(r'concert', ConcertViewSet)
router.register(r'piece', PieceViewSet)
router.register(r'soloist', SoloistViewSet)
router.register(r'musician', MusicianViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^', include(router.urls)),
]
