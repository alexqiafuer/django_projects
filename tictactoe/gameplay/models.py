from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse

GAME_STATUS_CHOICES = (
    ('F', 'First player to Move'),
    ('S', 'Second player to Move'),
    ('W', 'First player Wins'),
    ('L', 'Second player Wins'),
    ('D', 'Draw')
)

class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(
            Q(first_player=user) or Q(second_player=user)
        )
    
    def active(self):
        return self.filter(
            Q(status='F') or Q(status='S')
        )

class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="game_player_1", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="game_player_2", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

    objects = GamesQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("gameplay_detail", args=[self.id])
    

    def __str__(self):
        return f"{self.first_player} vs {self.second_player}"

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)