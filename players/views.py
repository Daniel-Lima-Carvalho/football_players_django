from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from players.models import Player
from django.shortcuts import redirect
from players.helpers import save_player
from django.core.paginator import Paginator

def index(request, page_number=1):
    players = Player.objects.all()
    paginator = Paginator(players, 4)
    actual_page = paginator.page(page_number)
    actual_player_list = actual_page.object_list
    next_page = actual_page.next_page_number() if actual_page.has_next() else None
    previous_page = actual_page.previous_page_number() if actual_page.has_previous() else None

    context = {
        'players': players,
        'paginator': paginator,
        'actual_player_list': actual_player_list,
        'next_page': next_page,
        'previous_page': previous_page
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