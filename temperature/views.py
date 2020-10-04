from rest_framework import generics
import datetime
import pandas as pd

from .serializers import TemperatureSerializer
from .models import Temperature


class TemperatureList(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def get_queryset(self):
        start_time = self.request.query_params.get("start_time")
        end_time = self.request.query_params.get("end_time")
        # step = self.request.query_params.get('step')

        time_range = Temperature.objects.filter(
            time__range=(start_time, end_time)
        ).order_by("-time")

        new_dict = {}
        for x in list(time_range.values()):
            date = str(x["time"])[:10]
            new_dict[datetime.datetime.strptime(date, "%Y-%m-%d")] = x["temperature"]
        avg_df = pd.DataFrame(new_dict, index=[0]).mean()
        avg_dict = avg_df.to_dict()

        queryset = time_range

        return queryset
