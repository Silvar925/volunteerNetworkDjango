from django.shortcuts import render
from rest_framework import generics
from .serializer import NewsSerializer, EventsSerializer, SpeakerSerializer
from .models import News, Events, Speaker


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class EventsAPIViews(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class SpeakerAPIViews(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer