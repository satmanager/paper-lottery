# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from lottery.models import Contestant 

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class ContestantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contestant
        fields = ('id','email','name', 'lastname', 'rut', 'url')

