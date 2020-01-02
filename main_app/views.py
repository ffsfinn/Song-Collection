from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Song:
    def __init__(self, name, artist, description, year):
        self.name = name
        self.artist = artist
        self.description = description
        self.year = year

songs = [
    Song('Midnight Hour', 'Skrillex', 'Recent Drop', 2019),
    Song('Bangarang', 'Skrillex', 'Older Song', 2011)
]

# Define the home view
def home(request):
  return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def songs_index(request):
    return render(request, 'songs/index.html', { 'songs': songs })