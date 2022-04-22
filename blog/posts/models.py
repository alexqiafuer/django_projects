from dataclasses import dataclass
from datetime import datetime

from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)