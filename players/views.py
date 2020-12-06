from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'player': 'Daniel Lima Carvalho',
    }
    return render(request, 'players/index.html', context)

def create(request):
    return render(request, 'players/create.html')