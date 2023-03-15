from django.conf.urls.static import static
from django.urls import path

from virus0check import settings
from .views import *
from . import views

#urlpatterns = [
#    path('', index),
#    path('result/', result),
#]

urlpatterns = [
    path('', views.file_upload_view, name='file_upload_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


