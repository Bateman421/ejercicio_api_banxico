from django.db import models


# Create your models here.
class Dates(models.Model):
    Fecha_inicial = models.DateField()
    Fecha_final = models.DateField()
