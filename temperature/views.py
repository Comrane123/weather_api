from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import TemperatureSerializer
from .models import Temperature


class TemperatureList(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        step = self.request.query_params.get('step')

        queryset = Temperature.objects.filter(time__range=(start_time, end_time)).order_by('-time')

        return queryset
