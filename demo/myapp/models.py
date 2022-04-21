from operator import mod
from pyexpat import model
from tracemalloc import is_tracing
from xmlrpc.client import boolean
from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    is_true = models.BooleanField(default=True)