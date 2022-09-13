from django import template
from app_movies.models import Genre, Movie

register = template.Library()

# данный тег только в качестве примера, функционал можно заменить классом GetGenreYearActor
@register.simple_tag()
def get_genres_header():
    return Genre.objects.all()


@register.inclusion_tag('tags/last_movies.html')
def get_last_movies(count=5):
    last_movies = Movie.objects.order_by('-id')[:count]
    return {'last_movies': last_movies}


@register.inclusion_tag('tags/linked_list.html')
def get_linked_list(my_list):
    return {'my_list': my_list}
