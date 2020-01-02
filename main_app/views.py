from django.shortcuts import render
from .models import Song

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def songs_index(request):
  songs = Song.objects.all()
  return render(request, 'songs/index.html', { 'songs': songs })

def songs_detail(request, songs_id):
  songs = Song.objects.get(id=songs_id)
  return render(request, 'songs/detail.html', { 'songs': songs })