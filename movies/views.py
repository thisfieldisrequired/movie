from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

movies_data = {1: 'The Dark Knight', 2: '12 Angry Men', 3: 'Il buono, il brutto, il cattivo'}


def movie_view(request, movie_id):
    context = movies_data.get(movie_id)
    return render(request, "movies/index.html", {'context': context})


def example_view(request):
    data = "HO!"
    return render(request, "movies/example.html", context={'first': data})


def custom_handler_404(request, exception):
    return HttpResponseNotFound("This page is not found")


