from django.contrib import admin
from .models import Event_Type, Event



@admin.register(Event_Type)
class Event_TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'event_link', 
                    'created', 'active']
                    
    list_filter = ['name', 'created']
    list_editable = ['event_link', 'active']
    prepopulated_fields = {'slug': ('name',)}
