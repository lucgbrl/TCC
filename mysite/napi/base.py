from django.utils import timezone
from django.conf import settings
from django.db import models

class BaseTemplate(models.Model):
    id = models.IntegerField('')
