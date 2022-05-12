from django.urls import path

from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', getRoutes),
    path('projects/', getProjects), 
    path('projects/<str:pk>', getProjects), 
]
