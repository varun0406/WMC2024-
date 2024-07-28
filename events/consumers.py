# import json
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import sync_to_async
# # consumers.py
# import json
# from channels.generic.websocket import WebsocketConsumer
# from .models import Venue, Organization, Event
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .forms import VenueForm, OrganizationForm, EventForm
# class AdminConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         print(data)
#         if data["action"]=="Update":
#             if data["venue_name"]:
#                  venue_form = VenueForm()
                
#         # if data['type'] == 'new':
#             # Handle the new item (e.g., save it to the database)
            

#     async def send_updates(self, model):
#         # Fetch the updated list of items from the database
#         items = await self.get_items(model)
#         await self.send(text_data=json.dumps({
#             'type': 'update',
#             'model': model,
#             'items': items
#         }))

#     async def get_items(self, model):
#         # Fetch items from the database based on the model
#         if model == 'venue':
#             items = await sync_to_async(list)(Venue.objects.all().values('id', 'venue_name', 'edit_url', 'delete_url'))
#         elif model == 'organization':
#             items = await sync_to_async(list)(Organization.objects.all().values('id', 'org_name', 'edit_url', 'delete_url'))
#         elif model == 'event':
#             items = await sync_to_async(list)(Event.objects.all().values('id', 'event_name', 'edit_url', 'delete_url'))
#         return items


# # class AdminConsumer(WebsocketConsumer):
# #     def connect(self):
# #         self.accept()

# #     def disconnect(self, close_code):
# #         pass

# #     def receive(self, text_data):
# #         text_data_json = json.loads(text_data)
# #         action = text_data_json['action']

# #         if action == 'create_venue':
# #             # Handle venue creation
# #             venue_data = text_data_json['venue']
# #             # Your logic to save the venue
# #             self.send(text_data=json.dumps({
# #                 'message': 'Venue created successfully!'
# #             }))
# #         elif action == 'create_organization':
# #             # Handle organization creation
# #             org_data = text_data_json['organization']
# #             # Your logic to save the organization
# #             self.send(text_data=json.dumps({
# #                 'message': 'Organization created successfully!'
# #             }))
# #         elif action == 'create_event':
# #             # Handle event creation
# #             event_data = text_data_json['event']
# #             # Your logic to save the event
# #             self.send(text_data=json.dumps({
# #                 'message': 'Event created successfully!'
# #             }))
