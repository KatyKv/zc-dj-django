from django.urls import path
from . import views

app_name = 'dj04_movies'

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:pk>/', views.movie_detail, name='movie_detail'),
    path('add_movie/', views.add_movie, name='add_movie')
]