from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class EventsHomeView(TemplateView):
    template_name = 'events/base.html'

events_home = EventsHomeView.as_view()
