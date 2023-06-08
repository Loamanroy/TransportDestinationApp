from rest_framework import serializers
from .models import Location, Car, Cargo


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    pick_up_location = LocationSerializer()
    delivery_location = LocationSerializer()

    class Meta:
        model = Cargo
        fields = '__all__'
