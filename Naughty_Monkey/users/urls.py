from django.urls import path

from .views import profiles, userProfile, loginUser, logoutUser, registerUser, userAccount, editAccount, createSkill, updateSkill, deleteSkill

urlpatterns = [
    path('', profiles, name='profiles'),
    path('profile/<str:pk>', userProfile, name='user-profile'),
    path('user-login', loginUser, name='user-login'),
    path('user-logout', logoutUser, name='user-logout'),
    path('user-register', registerUser, name="user-register"),
    path('user-account', userAccount, name='user-account'),
    path('user-edit', editAccount, name='user-edit'),
    path('create-skill', createSkill, name='create-skill'),
    path('update-skill/<str:pk>', updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>', deleteSkill, name='delete-skill')
]
