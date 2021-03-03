from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/movies/<str:title>', get_movie, name='getmovies'),
]