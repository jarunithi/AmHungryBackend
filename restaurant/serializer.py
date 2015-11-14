from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from restaurant.models import Restaurant


class RestaurantSerializer(ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'price', 'type',
                  'open_time', 'close_time', 'location_x',
                  'location_y', 'vote', 'pic')


class RequestSerializer(serializers.Serializer):
    price = serializers.IntegerField(min_value=0)
    res_type = serializers.CharField(max_length=200)
    user_x = serializers.FloatField()
    user_y = serializers.FloatField()
