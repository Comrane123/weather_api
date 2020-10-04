from datetime import datetime

import factory
import pytz

from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import Temperature


# Defining a factory
class TemperatureFactory(DjangoModelFactory):
    class Meta:
        model = Temperature

    time = factory.fuzzy.FuzzyDateTime(
        datetime(2020, 1, 1, 0, 0, 0, 0, pytz.UTC),
        force_minute=0,
        force_second=0,
        force_microsecond=0,
    )
    temperature = factory.fuzzy.FuzzyDecimal(0, 40, 1)
