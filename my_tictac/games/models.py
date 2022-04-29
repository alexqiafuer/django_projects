from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

BOARD_SIZE = 3

class game(models.Model):
    # initial game is player1 vs player2
    player_1 = models.ForeignKey(User, related_name='game_player_1', on_delete=models.CASCADE())
    player_2 = models.ForeignKey(User, related_name='game_player_2', on_delete=models.CASCADE())
    created = models.DateTimeField(auto_now_add=True)
    end_game = models.BooleanField(verbose_name='End of Game?', default=False)
    move_p1 = models.BooleanField(verbose_name='Player 1 to move?', default=False)

    def board(self):
        board = [[''] * range(BOARD_SIZE) for _ in range(BOARD_SIZE)]

        return board

class Move(models.Model):
    x = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE - 1)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE - 1)]
    )