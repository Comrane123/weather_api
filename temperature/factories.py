import factory
from factory.django import DjangoModelFactory

from .models import Temperature


# Defining a factory
class TemperatureFactory(DjangoModelFactory):
    class Meta:
        model = Temperature

    time = factory.Faker("date_time")
    temperature = factory.Faker("random_digit_not_null")
