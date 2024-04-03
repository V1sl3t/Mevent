from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope.get("user").is_anonymous:
            await self.close()

        self.group_name = str(self.scope.get("user").pk)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")

        await self.send(text_data=json.dumps({
            "message": message,
        }))

    async def follow(self, event):
        await self.send(text_data=json.dumps(event))

    async def follow_request(self, event):
        await self.send(text_data=json.dumps(event))

    async def accept_follow_request(self, event):
        await self.send(text_data=json.dumps(event))
