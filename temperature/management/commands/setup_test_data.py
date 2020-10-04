from django.db import transaction
from django.core.management.base import BaseCommand

from temperature.models import Temperature
from temperature.factories import TemperatureFactory

NUM_TEMPERATURES = 100


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Temperature]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the users
        times = []
        temperatures = []

        for _ in range(NUM_TEMPERATURES):
            time = TemperatureFactory()
            temperature = TemperatureFactory()

            times.append(time)
            temperatures.append(temperature)
