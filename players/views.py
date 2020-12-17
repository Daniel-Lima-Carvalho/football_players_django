from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from players.models import Player
from django.shortcuts import redirect

def index(request):
    context = {
        'players': Player.objects.all()
    }
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

def delete(request, id):
    player = Player.objects.get(pk=id)
    player.delete()
    return redirect('index')
