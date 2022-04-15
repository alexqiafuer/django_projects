from datetime import time
from email.policy import default
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField(default=0)
    room = models.IntegerField(default=101)

    def __str__(self):
        return f"{self.name} at floor {self.floor} in room {self.room}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(11))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def  __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

