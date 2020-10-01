from rest_framework import generics

from .serializers import TemperatureSerializer
from .models import Temperature


class TemperatureList(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
