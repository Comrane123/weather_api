from django.db import models


class Temperature(models.Model):
    time = models.DateTimeField()
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.time} - {self.temperature}"
