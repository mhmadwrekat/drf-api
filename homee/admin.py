from django.contrib import admin
from .models import Thing

@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin) :
    list_displaty = ['name', 'type', 'content', 'timestamp', 'updated', 'author', 'published']
