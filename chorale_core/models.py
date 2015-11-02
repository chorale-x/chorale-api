from django.db import models
from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')


class Comment(models.Model):
    name = models.CharField(max_length=254, blank=True)
    message = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        