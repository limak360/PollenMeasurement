from django.db import models

# Create your models here.

class PollenMeasurement(models.Model):
    pollen_type = models.CharField(max_length=100)
    pollen_count = models.CharField(max_length=200)
    measurement_location = models.CharField(max_length=200)
    measurement_time = models.DateTimeField('measurement_time')
