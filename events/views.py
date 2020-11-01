from django.shortcuts import render
from django.views.generic import ListView
from .models import Event_Type, Event

class HomeView(ListView):
    model = Event
    paginate_by = 3
    template_name = "events/events.html"
