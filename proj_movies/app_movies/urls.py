from django.urls import path
from app_movies.views import MovieListView, MovieDetailView, AddComment

urlpatterns = [
    path('', MovieListView.as_view(), name='main'),
    path('<slug:slug>', MovieDetailView.as_view(), name='movie'),
    path('reviews/<int:pk>', AddComment.as_view(), name='add_review')
]