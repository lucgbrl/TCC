from django.db import models

# Create your models here.
# Classes do projeto
class PAI(models.Model):
    cod = models.CharField(max_length=10)
    desc = models.CharField(max_length=20)
    