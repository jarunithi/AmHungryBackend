from rest_framework.serializers import ModelSerializer
from restaurant.models import Restaurant


class RestaurantSerializer(ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'price', 'type',
                  'open_time', 'close_time', 'location_x',
                  'location_y', 'vote', 'rc_point')
