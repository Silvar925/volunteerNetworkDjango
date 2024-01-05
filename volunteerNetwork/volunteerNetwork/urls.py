from django.contrib import admin
from django.urls import path, include
from VNCore.urls import urlpatternsVNCore
from personalProfile.urls import urlpatternsPersonalProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatternsVNCore)),
    path('', include(urlpatternsPersonalProfile))
]
