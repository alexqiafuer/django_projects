from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room', views.room_create, name='create-room'),
    path('update-room/<str:pk>', views.room_update, name='update-room'),
    path('delete-room/<str:pk>', views.room_delete, name='delete-room')
]
