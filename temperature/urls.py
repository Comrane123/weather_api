from django.urls import path

from .views import TemperatureList

urlpatterns = [
    path("", TemperatureList.as_view()),
]
