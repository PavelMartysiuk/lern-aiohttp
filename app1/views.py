from aiohttp_rest_framework import views

from app1.serializers import UserSerializer, ItemSerializer

from publisher import Publisher

import json


class Abstract:

    @staticmethod
    async def publisher_send_message(message):
        pub = Publisher(connect="nats://0.0.0.0:4222", message=message)
        await pub.send_message()


class UsersListCreateView(views.ListCreateAPIView, Abstract):
    serializer_class = UserSerializer

    async def get(self):
        message = f'{self.request.host} + {self.request.method}'
        await self.publisher_send_message(message)
        return await super().get()

    async def post(self):
        message = await self.request.json()
        await self.publisher_send_message(json.dumps(message))
        return await super().post()


class UsersRetrieveUpdateDestroyView(views.RetrieveUpdateDestroyAPIView, Abstract):
    serializer_class = UserSerializer

    async def get(self):
        message = f'{self.request.host} + {self.request.method}'
        await self.publisher_send_message(message)
        return await super().get()

    async def put(self):
        message = await self.request.json()
        await self.publisher_send_message(json.dumps(message))
        return await super().put()

    async def patch(self):
        message = await self.request.json()
        await self.publisher_send_message(json.dumps(message))
        return await super().patch()


class ItemsListCreateView(views.ListCreateAPIView, Abstract):
    serializer_class = ItemSerializer

    async def get(self):
        message = f'{self.request.host} + {self.request.method}'
        await self.publisher_send_message(message)
        return await super().get()

    async def post(self):
        message = await self.request.json()
        await self.publisher_send_message(json.dumps(message))
        return await super().post()


class ItemsRetrieveUpdateDestroyView(views.RetrieveUpdateDestroyAPIView, Abstract):
    serializer_class = ItemSerializer

    async def get(self):
        message = f'{self.request.host} + {self.request.method}'
        await self.publisher_send_message(message)
        return await super().get()

    async def put(self):
        message = await self.request.json()
        await self.publisher_send_message(json.dumps(message))
        return await super().put()

    async def patch(self):
        message = await self.request.json()
        await self.publisher_send_message(json.dumps(message))
        return await super().patch()
