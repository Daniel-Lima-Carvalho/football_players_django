from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from players.models import Player
from django.shortcuts import redirect
from players.helpers import save_player

def index(request):
    context = {
        'players': Player.objects.all()
    }
    return render(request, 'players/index.html', context)

def create(request):
    if request.method == 'POST':
        player = Player()
        player = save_player(request, player)
    return render(request, 'players/create.html')

def update(request, id):
    player = Player.objects.get(pk=id)

    if request.POST.get('method') == 'PUT':
        player = save_player(request, player)
        
    context = { 'player': player }
    return render(request, 'players/update.html', context)

def delete(request, id):
    player = Player.objects.get(pk=id)
    player.delete()
    return redirect('index')