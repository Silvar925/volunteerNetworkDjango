from django.contrib import admin
from django.urls import path
from . import views

urlpatternsVNCore = [
    path('listNews', views.NewsAPIView.as_view(), name='listNews'),
    path('listEvents', views.EventsAPIViews.as_view(), name='listEvents'),
    path('listSpeakers', views.SpeakerAPIViews.as_view(), name='listSpeakers')
]
