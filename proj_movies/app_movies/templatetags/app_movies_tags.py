from django import template
from app_movies.models import Genre, Movie

register = template.Library()

@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.inclusion_tag('tags/last_movies.html')
def get_last_movies(count=5):
    last_movies = Movie.objects.order_by('-id')[:count]
    return {'last_movies': last_movies}