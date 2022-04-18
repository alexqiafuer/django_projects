from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import game_detail

urlpatterns = [
    path('detail/<int:id>', game_detail, name="gameplay_detail")
]