from django.contrib import admin
from django.urls import path
from . import views

urlpatternsPersonalProfile = [
    path('personalProfile', views.personalProfile, name='personalProfile'),
    path('authentication', views.authentication, name='authentication'),
    path('verification', views.user_login, name='verification'),
    path('register', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
