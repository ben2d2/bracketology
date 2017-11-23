# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)

class Team(models.Model):
    name = models.CharField(max_length=200)
    seed = models.IntegerField(default=0)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class GameTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Game(models.Model):
    game_round = models.IntegerField(default=0)
