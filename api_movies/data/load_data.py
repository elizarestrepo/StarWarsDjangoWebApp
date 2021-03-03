from ..models import Character, Movie
import requests

class LoadData():

    def get_characters():
        url='https://swapi.dev/api/people'
        result = requests.get(url).json()
        data = result['results']
        for person in data:
            name_character=person['name']
            create_character, created = Character.objects.update_or_create(
                name=person['name'], 
                birth_year=person['birth_year'], 
                gender=person['gender'],
                imagen='images/characters/' + name_character.replace(' ','_') + '.jpg',
                url=person['url'])
    
    def get_movies():
        url='https://swapi.dev/api/films'
        result = requests.get(url).json()
        data = result['results']
        for film in data:
            create_movie = Movie(
                title=film['title'],
                episode_id=film['episode_id'],
                resume=film['opening_crawl'],
                director=film['director'],
                producer=film['producer'],
                release_date=film['release_date'],
                url=film['url'])
            
            create_movie.save()

            for person in film['characters']:
                if Character.objects.filter(url=person).exists():
                    create_movie.characters.add(Character.objects.get(url=person))
