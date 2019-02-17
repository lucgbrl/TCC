from django.db import models

# Create your models here.
class PAI(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero_registro = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)


class Acomp_pressao_arterial_glicemia(models.Model):
    responsavel = models.ForeignKey("responsavel pela solicitação", settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pai = models.ForeignKey("Pai", 'PAI', on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(blank=True, null=True)
    dia = models.DateTimeField("Dia",default=timezone.now)
    turno = models.CharField("Turno")
    hora = models.DateTimeField("Hora",default=timezone.now)
    PA = models.CharField("PA", max_lengyh = 10)
    Dx = models.CharField("Dx", max_lengyh = 10)
    observacao = models.TextField("Observação")


    def solicitacao(self):
        self.data_solicitacao = timezone.now()
        self.save()

    def __str__(self):
        return self.title
