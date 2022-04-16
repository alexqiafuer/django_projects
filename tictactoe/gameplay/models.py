from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="game_player_1", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="game_player_2", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F')

    def __str__(self):
        return f"{self.first_player} vs {self.second_player}"

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)