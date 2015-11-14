from django.db import models

# Create your models here.


class Restaurant(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=2000)
    type = models.CharField(max_length=2000)
    open_time = models.TimeField()
    close_time = models.TimeField()
    location_x = models.FloatField()
    location_y = models.FloatField()
    rc_point = models.FloatField()
    vote = models.FloatField()
    pic = models.URLField(max_length=200, null=True)
