import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import roomapp.routing  # adjust as per your app name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogweb.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            roomapp.routing.websocket_urlpatterns
        )
    ),
})
