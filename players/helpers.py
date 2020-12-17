def save_player(request, player):
    player.name = request.POST.get('name')
    player.team = request.POST.get('team')
    player.position = request.POST.get('position')
    player.picture = request.POST.get('picture')
    player.save()
    return player