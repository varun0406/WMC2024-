import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wmcgta.settings')

# Ensure Django is set up
django.setup()

# Import your routing only after Django is set up
import Donation_STATS.routing

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Django setup complete")

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Donation_STATS.routing.websocket_urlpatterns
        )
    ),
})

logger.info("ASGI application loaded")
