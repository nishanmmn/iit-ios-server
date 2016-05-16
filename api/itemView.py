from django.shortcuts import render
from rest_framework import viewsets
from api.itemModel import item
from itemSerializer import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
	queryset=item.objects.all()
	serializer_class=ItemSerializer