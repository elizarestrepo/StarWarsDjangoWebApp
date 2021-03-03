from .models import Character, Movie
from rest_framework import serializers

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'episode_id', 'resume', 'director', 'producer', 'release_date', 'imagen', 'characters']