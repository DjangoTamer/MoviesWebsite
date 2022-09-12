from django.urls import path
from app_movies.views import MovieListView, MovieDetailView, PersonDetailView, AddComment

urlpatterns = [
    path('', MovieListView.as_view(), name='main'),
    path('<slug:slug>', MovieDetailView.as_view(), name='movie'),
    path('persons/<slug:slug>', PersonDetailView.as_view(), name='actor'),
    path('reviews/<int:pk>', AddComment.as_view(), name='add_review'),
]