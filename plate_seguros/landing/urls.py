from django.urls import path

from plate_seguros.settings import MEDIA_ROOT
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]