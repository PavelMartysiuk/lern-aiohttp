from aiohttp_rest_framework import serializers

from app1.tables import users, items


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = '__all__'
