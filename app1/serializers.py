from aiohttp_rest_framework import serializers

from app1.tables import User, Items


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('add_date',)
        model = User.__table__
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items.__table__
        fields = '__all__'
