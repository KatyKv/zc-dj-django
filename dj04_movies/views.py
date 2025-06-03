from django.shortcuts import render, redirect, get_object_or_404

from .models import Movies
from .forms import MovieForm


def index(request):
    movies = Movies.objects.all()
    return render(
        request,
        'dj04_movies/index.html',
        {'movies': movies}
    )

def movie_detail(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    movie_list = list(Movies.objects.all().order_by('id'))

    current_index = next(i for i, m in enumerate(movie_list) if m.pk == movie.pk)

    prev_movie = movie_list[current_index - 1] if current_index > 0 else None
    next_movie = movie_list[current_index + 1] if current_index < len(movie_list) - 1 else None

    return render(
        request,
        'dj04_movies/movie_detail.html',
        {'movie': movie,
                'prev_movie': prev_movie,
                'next_movie': next_movie,
                }
    )

def add_movie(request):
    error = ''
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            new_movie = form.save(commit=False)
            new_movie.save()
            return redirect('dj04_movies:index')
        else:
            error = 'Данные заполнены некорректно'
    form = MovieForm()
    return render(
        request,
        'dj04_movies/add_movie.html',
        {'form': form, 'error': error}
    )
