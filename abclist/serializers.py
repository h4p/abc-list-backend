from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ABCList


class ABCListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ABCList
        fields = ['id', 'user', 'abclist', 'created_at', 'updated_at']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
