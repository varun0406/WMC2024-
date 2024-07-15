from channels.generic.websocket import AsyncWebsocketConsumer
import json

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
