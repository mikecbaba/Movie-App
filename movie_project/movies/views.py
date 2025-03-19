from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if movie.user == request.user:
        # Delete the poster image file
        poster_path = os.path.join(settings.MEDIA_ROOT, str(movie.poster))
        if os.path.isfile(poster_path):
            os.remove(poster_path)

        # Delete the movie object
        movie.delete()
    return redirect('movie_list')

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
