import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

import samolotApp


class Lot(models.Model):
    title = models.CharField(max_length=200)
    StartDate = models.DateField(default=datetime.date.today)
    Destination = models.CharField(max_length=200)
    samolot = models.ForeignKey("samolotApp.Samolot", on_delete=models.CASCADE)
