from django.shortcuts import render
from rest_framework import viewsets
from api.userModel import user
from userSerializer import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset=user.objects.all()
	serializer_class=UserSerializer