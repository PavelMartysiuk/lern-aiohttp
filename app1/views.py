from aiohttp_rest_framework import views

from app1.serializers import UserSerializer, ItemSerializer


class UsersListCreateView(views.ListCreateAPIView):
    serializer_class = UserSerializer


class UsersRetrieveUpdateDestroyView(views.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer


class ItemsListCreateView(views.ListCreateAPIView):
    serializer_class = ItemSerializer


class ItemsRetrieveUpdateDestroyView(views.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
