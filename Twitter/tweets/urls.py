from django.urls import path

from .views import welcome_view, tweet_detail_view, tweet_list_view, tweet_create_view

urlpatterns = [
    path('', welcome_view),
    path('create-tweet', tweet_create_view),
    path('tweets', tweet_list_view),
    path('tweets/<int:tweet_id>', tweet_detail_view)
]
