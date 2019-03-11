#ava.py reune informações de classes de avaliação de diferentes ramos

from django.utils import timezone
from django.conf import settings
from django.db import models

class ava_clinica_med_sample(models.Model):
    #avaliação clínica, medidas e sampla
    data = models.DateTimeField(blank=True, null = True)
    #medidas
    peso = models.FloatField()
    altura = models.FloatField()
    TIPO_SANGUINEO = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )
    tipo_sanguineo = models.CharField(max_length = 3,choices = TIPO_SANGUINEO)
    