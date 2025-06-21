from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/blogchat/<slug:slug>/', consumers.BlogChatConsumer.as_asgi()),
]
