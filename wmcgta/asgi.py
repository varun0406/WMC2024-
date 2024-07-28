import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Donation_STATS.routing

#  Donation_STATS.routing.websocket_urlpatterns +
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wmcgta.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Donation_STATS.routing.websocket_urlpatterns 
            
        )
    ),
})
print(Donation_STATS.routing.websocket_urlpatterns)