from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    Description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['complete']

    def __str__(self) -> str:
        return self.title