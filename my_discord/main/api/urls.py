from django.urls import path

from .views import *

urlpatterns = [
    path('', get_routes),
    path('rooms/', getRooms),
    path('room/<str:pk>', getRoom),
]
