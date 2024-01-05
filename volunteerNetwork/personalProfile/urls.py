from django.contrib import admin
from django.urls import path
from . import views

urlpatternsPersonalProfile = [
    path('personalProfile', views.personalProfile, name='personalProfile'),
    path('authentication', views.authentication, name='authentication'),
]
