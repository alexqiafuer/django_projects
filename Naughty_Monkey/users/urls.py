from django.urls import path

from .views import profiles, userProfile, loginUser, logoutUser, registerUser, userAccount

urlpatterns = [
    path('', profiles, name='profiles'),
    path('profile/<str:pk>', userProfile, name='user-profile' ),
    path('user-login', loginUser, name='user-login'),
    path('user-logout', logoutUser, name='user-logout'),
    path('user-register', registerUser, name="user-register"),
    path('user-account', userAccount, name='user-account')
]
