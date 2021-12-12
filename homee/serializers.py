from rest_framework import serializers
from .models import Thing

class ThingSerializer(serializers.ModelSerializer) :
    class Meta :
        fields = ['name', 'type', 'content', 'timestamp', 'updated', 'author', 'published']
        model = Thing
