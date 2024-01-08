from django.contrib import admin
from django.urls import path
from . import views


urlpatternsVNCore = [
    path('', views.newsPage, name='news'),
    path('events', views.eventsPage, name='events'),
    path('rating', views.ratingPage, name='rating'),

    path('listNews', views.NewsAPIView.as_view(), name='listNews'),
    path('listRating', views.RatingAPIViews.as_view(), name='listRating'),
    path('listEvents', views.EventsAPIViews.as_view(), name='listEvents'),
    path('listSpeakers', views.SpeakerAPIViews.as_view(), name='listSpeakers'),
    path('listOrganizers', views.OrganizersAPIViews.as_view(), name='listOrganizers')
]

