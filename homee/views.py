from django.shortcuts import render
from rest_framework import generics
from .models import Thing
from.serializers import ThingSerializer

# CR views
class ThingList(generics.ListCreateAPIView) :

#    queryset = Thing.objects.all()
    queryset = Thing.objects.filter(published = True)
    serializer_class = ThingSerializer

# RUD view
class ThingDetail(generics.RetrieveUpdateDestroyAPIView) :

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
