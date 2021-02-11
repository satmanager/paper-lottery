from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from lottery.models import Contestant 
from .serializers import UserSerializer, ContestantSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    class Meta:
        app_label = 'lottery'


class ContestantViewSet(viewsets.ModelViewSet):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer

    class Meta:
        app_label = 'lottery'
