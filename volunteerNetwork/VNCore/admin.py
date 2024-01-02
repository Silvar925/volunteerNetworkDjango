from django.contrib import admin
from .models import News, Events, Speaker, Organizers

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'photo')
    search_fields = ['name', 'text', 'photo']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'photo')
    search_fields = ['name', 'text', 'photo']


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'photo')
    search_fields = ['name', 'bio', 'photo']


@admin.register(Organizers)
class OrganizersAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'photo')
    search_fields = ['name', 'bio', 'photo']