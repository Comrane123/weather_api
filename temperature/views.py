from rest_framework import generics, response
from statistics import mean
from collections import defaultdict
from rest_framework.response import Response

from .serializers import TemperatureSerializer
from .models import Temperature


class TemperatureList(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def get(self, request, *args, **kwargs):
        start_time = self.request.query_params.get("start_time")
        end_time = self.request.query_params.get("end_time")
        step = self.request.query_params.get("step")

        if start_time and end_time is not None:
            temp_dict = defaultdict(list)

            time_range = Temperature.objects.filter(
                time__range=(start_time, end_time)
            ).order_by("-time")

            for x in list(time_range.values()):
                date = str(x["time"].date())
                temp = x["temperature"]
                temp_dict[date].append(temp)

            for date in temp_dict:
                temp_dict[date] = mean(temp_dict[date])

            avg_temp = dict(temp_dict)

            return Response(avg_temp)

        else:
            return self.list(request, *args, **kwargs)
