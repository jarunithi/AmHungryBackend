from django.contrib import admin
from models import Restaurant
# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'type',
                    'open_time', 'close_time', 'location_x',
                    'location_y', 'vote', 'rc_point')

admin.site.register(Restaurant, RestaurantAdmin)
