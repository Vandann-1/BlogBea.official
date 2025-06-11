from django.urls import path
from .views import spotify_auth, spotify_callback

urlpatterns = [
    path('auth/', spotify_auth, name='auth'),
    path('spotify/callback/', spotify_callback, name='spotify-callback'),
]
