from django.utils import timezone
from django.conf import settings
from django.db import models

class Acompanhamento_de_Pressao_Arterial_Glicemia(models.Model):
    #cadastro de titulo
    cliente = models.CharField(max_length=200)

    #inteiros
    pai = models.ForeignKey("PAI", 'Prontuario_de_Atendimento_Integral_PAI' ,on_delete=models.CASCADE)

    #data e hora automatica
    data_de_solicitacao = models.DateTimeField(default=timezone.now)


    #cadastro de data do dia (campo do formulario)
    dia = models.DateTimeField(blank=True, null=True)

    #cadastro do turno e da hora (campo do formulario)
    turno = models.CharField(max_length = 64, blank=True, null=True))
    hora = models.DateTimeField(blank=True, null=True)

    #PA e Dx (Pressão e Glicemia)
    pa = models.CharField("PA",  null = True, blank = True)
    dx = models.CharField("Dx",  null = True, blank = True)

    #textos longos
    observacao = models.TextField("Observação", null = True, blank = True)



    #usuario que realiza o cadastro
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def publish(self):
        self.dia = timezone.now()
        self.dia = timezone.now()
        self.save()
    #######

    def __str__(self):
        return self.cliente

