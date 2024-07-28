# leaderboard/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from.models import Statistics
from django.core.serializers import serialize
from channels.generic.websocket import AsyncWebsocketConsumer
class LeaderboardConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'leaderboard_group'
        self.channel_layer = get_channel_layer()
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass

    def send_leaderboard(self):
        leaderboard_data = Statistics.objects.all().order_by('-value')
        data = serialize('json', leaderboard_data)
        self.send(text_data=json.dumps({
            'type': 'update',
            'data': data
        }))
class DashBoard(AsyncWebsocketConsumer):
    async def connect(self):
        self.slug = self.scope['url_route']['kwargs']['slug']
        print(f"Connected to {self.slug}")
        await self.accept()
    
    async def disconnect(self, close_code):
        print(f"Disconnected {close_code}")
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        print(f"Received {message} from {sender}")
        
        await self.send(text_data=json.dumps({
            'message':"helol from server "
            
        }))
