from django.urls import path


from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout' ),
    path('register/', views.user_register, name='register'),
    path('profile/<str:pk>', views.user_profile, name='user-profile' ),
    path('update-user', views.user_update, name='update-user'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room', views.room_create, name='create-room'),
    path('update-room/<str:pk>', views.room_update, name='update-room'),
    path('delete-room/<str:pk>', views.room_delete, name='delete-room'),
    path('delete-message/<str:pk>', views.message_delete, name='delete-message'),
]
