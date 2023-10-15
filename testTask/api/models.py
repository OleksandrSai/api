from django.db import models

# Create your models here.


class Counter(models.Model):
    serial_number = models.CharField(max_length=80, unique=True)
    model = models.CharField(max_length=250)
    manufacture_date = models.DateField()
    current_reading = models.IntegerField(blank=True)
    status = models.BooleanField(default=True)