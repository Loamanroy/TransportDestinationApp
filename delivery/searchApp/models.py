from django.db import models
from geopy.distance import distance


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


def get_distance_to_location(location):
    car_location = (location.latitude, location.longitude)
    target_location = (location.latitude, location.longitude)
    return distance(car_location, target_location).miles


class Car(models.Model):
    number = models.CharField(max_length=5, unique=True)
    current_location = models.CharField(max_length=100)
    capacity = models.IntegerField()


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, related_name='pick_up_cargos', on_delete=models.CASCADE)
    delivery_location = models.ForeignKey(Location, related_name='delivery_cargos', on_delete=models.CASCADE)
    weight = models.IntegerField()
    description = models.TextField()
