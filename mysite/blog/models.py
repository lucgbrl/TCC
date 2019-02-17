from django.conf import settings
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    #inteiros
    idade = models.IntegerField()
    #usuario que realiza o cadastro
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #cadastro de titulo
    title = models.CharField(max_length=200)

    #textos longos 
    text = models.TextField()

    #data e hora automatica
    created_date = models.DateTimeField(default=timezone.now)
   
    #cadastro de data
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #######

    def __str__(self):
        return self.title