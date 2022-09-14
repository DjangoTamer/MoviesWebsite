from django.urls import path
from app_movies.views import MovieListView, FilterMovieView, SearchMovieView, MovieDetailView, PersonDetailView, AddComment

urlpatterns = [
    path('', MovieListView.as_view(), name='main'),
    path('search/', SearchMovieView.as_view(), name='search_movie'),
    path('filter/', FilterMovieView.as_view(), name='filter_movie'),
    path('<slug:slug>', MovieDetailView.as_view(), name='movie'),
    path('persons/<slug:slug>', PersonDetailView.as_view(), name='person'),
    path('reviews/<int:pk>', AddComment.as_view(), name='add_review'),
]