from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'players': [{'name': 'Daniel','team': 'Flamengo'},{'name': 'Daniel 2','team': 'Flamengo'}]
    }
    return render(request, 'players/index.html', context)

def create(request):
    return render(request, 'players/create.html')