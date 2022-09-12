from django.shortcuts import render, redirect
from app_movies.models import Movie, Person
from app_movies.forms import CommentForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


class MovieListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(published=True)
    template_name = 'app_movies/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'slug'

class PersonDetailView(DetailView):
    model = Person
    slug_field = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_key'] = 8
        return context



class AddComment(View):
    def post(self, request, pk):
        print(request.POST)
        form = CommentForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())



'''
# Functions Views for example
def show_movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'app_movies/movie_list.html', context={'movies': movies})

def show_movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, 'app_movies/movie_detail.html', context={'movie': movie})
'''

