from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    picture = models.CharField(max_length=1000, blank=True)
