from django.conf.urls.static import static
from django.urls import path

from virus0check import settings
from .views import *

urlpatterns = [
    path('', index),
    path('result/', result),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

