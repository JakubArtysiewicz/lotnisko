import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Linia(models.Model):
    nazwa = models.TextField(max_length=200)
    rok_powstania = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(datetime.date.today().year)])

class Marka(models.Model):
    nazwa = models.TextField(max_length=200)
    rok_powstania = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(datetime.date.today().year)])

class Przeznaczenie(models.Model):
    przeznaczenie = models.TextField()

class Czesc(models.Model):
    nazwa = models.TextField(max_length=200)
    nr_katologowy = models.TextField(max_length=200)

class Zabezpieczenia(models.Model):
    nazwa = models.TextField(max_length=200)
    nr_katalogowy_czesci = models.ForeignKey(Czesc ,on_delete=models.CASCADE)

class Typ(models.Model):
    nazwa = models.TextField(max_length=200)
    zabezpieczenia = models.ForeignKey(Zabezpieczenia, on_delete=models.CASCADE)
    wielkosc = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    przeznaczenie = models.ForeignKey(Przeznaczenie, on_delete=models.CASCADE)

class ModelNazwa(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    nazwa = models.TextField(max_length=200)
    typ = models.ForeignKey(Typ, on_delete=models.CASCADE)

class Samolot(models.Model):
    model = models.ForeignKey(ModelNazwa, on_delete=models.CASCADE)
    linia = models.ForeignKey(Linia, on_delete=models.CASCADE)
    nr_rejestracyjny = models.TextField(max_length=200)

