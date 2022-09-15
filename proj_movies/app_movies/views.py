from django.shortcuts import render, redirect
from app_movies.models import Movie, Person, Genre
from app_movies.forms import CommentForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.db.models import Q


class GetGenreYearActor:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.all().values('year').distinct().order_by('-year')

    # def get_actors(self):
    #     return Person.movie_set.actor.all()

    # def get_directors(self):
    #     return Person.movie_set.director.all()


class MovieListView(GetGenreYearActor, ListView):
    model = Movie
    queryset = Movie.objects.filter(published=True)
    template_name = 'app_movies/movie_list.html'
    paginate_by = 6


class MovieDetailView(GetGenreYearActor, DetailView):
    model = Movie
    queryset = Movie.objects.filter(published=True)
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PersonDetailView(GetGenreYearActor, DetailView):
    model = Person
    slug_field = 'slug'


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


class FilterMovieView(GetGenreYearActor, ListView):
    paginate_by = 3

    def get_queryset(self):
        years_list = self.request.GET.getlist('year')
        genres_list = self.request.GET.getlist('genre_id')
        queryset = Movie.objects.filter(published=True)
        if years_list and genres_list:
            queryset = queryset.filter(Q(year__in=years_list) & Q(genre__in=genres_list))
        else:
            queryset = queryset.filter(Q(year__in=years_list) | Q(genre__in=genres_list))
        # queryset = Movie.objects.filter(year__in=self.request.GET.getlist('year'))
        return queryset.distinct()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['year'] = ''.join([f'year={x}&' for x in self.request.GET.getlist('year')])
        context['genre'] = ''.join([f'genre_id={x}&' for x in self.request.GET.getlist('genre_id')])
        return context


class SearchMovieView(GetGenreYearActor, ListView):
    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('s')
        # в данной БД не работает icontains, поэтому сделал костыль для увеличения совпадений
        queryset = Movie.objects.filter(Q(name__contains=search.lower()) | Q(name__contains=search.capitalize()))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = f"s={self.request.GET.get('s')}&"
        return context


# альтернатива - flatpages django
def show_contacts(request):
    return render(request, 'app_movies/contacts.html')

'''
# Functions Views for example
def show_movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'app_movies/movie_list.html', context={'movies': movies})

def show_movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, 'app_movies/movie_detail.html', context={'movie': movie})
'''
