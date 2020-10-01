from rest_framework import serializers

from temperature.models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = [
            "time",
            "temperature",
        ]
