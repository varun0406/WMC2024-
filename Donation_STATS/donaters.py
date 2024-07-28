from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.serializers import serialize
from .models import Statistics
import json

class LeaderboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("leaderboard_group", self.channel_name)
        await self.send_leaderboard()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("leaderboard_group", self.channel_name)

    async def receive(self, text_data):
        pass

    @sync_to_async
    def get_leaderboard_data(self):
        return list(Statistics.objects.all())

    async def send_leaderboard(self):
        leaderboard_data = await self.get_leaderboard_data()
        data = serialize('json', leaderboard_data)
        await self.send(text_data=json.dumps({
            'type': 'update',
            'data': data
        }))

    # Handler for send_leaderboard_update message type
    async def send_leaderboard_update(self, event):
        await self.send_leaderboard()

# Function to send leaderboard update to the group
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver

def send_leaderboard_update():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'leaderboard_group',
        {
            'type': 'send_leaderboard_update',
        }
    )

@sync_to_async
def fetch_leaderboard_data():
    return list(Statistics.objects.all())

@receiver(post_save, sender=Statistics)
def statistics_changed(sender, instance, **kwargs):
    send_leaderboard_update()
