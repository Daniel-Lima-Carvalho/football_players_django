from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from players.models import Player

def index(request):
    context = {
        'players': Player.objects.all()
    }
     #'players': [{'name': 'Daniel','team': 'Flamengo','position': 'Midfielder'},{'name': 'Daniel 2','team': 'Flamengo','position': 'Midfielder'}]

    return render(request, 'players/index.html', context)

def create(request):
    if request.method == 'POST':
        player = Player()
        player.name = request.POST.get('name')
        player.team = request.POST.get('team')
        player.position = request.POST.get('position')
        player.picture = request.POST.get('picture')
        player.save()
        return render(request, 'players/create.html')
    return render(request, 'players/create.html')

def update(request):
    return render(request, 'players/update.html')