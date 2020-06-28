from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Menu


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'first_name', 'last_name', 'is_active', 'groups')


class UserSerializerDepth(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 2


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class GroupSerializerDepth(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

