from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest.serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    # api for users to be created and edited
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    # api for viewing all groups
    queryset=Group.objects.all()
    serializer_class = GroupSerializer

