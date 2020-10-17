from django.shortcuts import render
from rest_framework import viewsets
#import django_filters

from .models import Item
from .serializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
