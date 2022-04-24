from operator import mod
from django.contrib import admin

from .models import Task

admin.site.register(Task)