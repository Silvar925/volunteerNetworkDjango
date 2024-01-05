from django.shortcuts import render
from rest_framework import generics
from .serializer import NewsSerializer, EventsSerializer, SpeakerSerializer, RatingSerializer
from .models import News, Events, Speaker, Organizers, Rating


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class EventsAPIViews(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class SpeakerAPIViews(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


class OrganizersAPIViews(generics.ListAPIView):
    queryset = Organizers.objects.all()
    serializer_class = SpeakerSerializer


class RatingAPIViews(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


def eventsPage(request):
    return render(request, 'VNCore/events.html')

def newsPage(request):
    return render(request, 'VNCore/index.html')

def ratingPage(request):
    return render(request, 'VNCore/rating.html')