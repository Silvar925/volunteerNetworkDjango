from django.contrib import admin
from django.urls import path, include
from VNCore.urls import urlpatternsVNCore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatternsVNCore))
]
