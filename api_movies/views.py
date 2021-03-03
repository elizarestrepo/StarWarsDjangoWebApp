from django.shortcuts import render
from .serializers import CharacterSerializer, MovieSerializer
from .models import Character, Movie
from .data.load_data import LoadData

def index(request):
    if not Character.objects.exists():
        LoadData.get_characters()
    if not Movie.objects.exists():
        LoadData.get_movies()
    serialize = CharacterSerializer(Character.objects.all(), many=True)
    return render(request, 'movies/movies.html', {'data':serialize.data})


