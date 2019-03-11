#ava.py reune informações de classes de avaliação de diferentes ramos
from django.utils import timezone
from django.conf import settings
from django.db import models
from .models import Prontuario_de_Atendimento_Integral_PAI

#este documento importa o PAI como classe fundamental pois ele é a base para a maioria dos formulários

class ava_clinica_med_sample(models.Model):
    #avaliação clínica, medidas e sampla

    #começa com medidas
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
    tipo_sanguineo = models.CharField(max_length = 3, choices = TIPO_SANGUINEO)
    pa = models.CharField("PA", max_length=32)
    dx = models.CharField("DX", max_length=32)
    fr = models.CharField("FR", max_length=32)
    pulso = models.CharField("Pulso" , max_length = 32)
    #sampla
    sinais_sintomas = models.TextField("Sinais e sintomas")
    alergias = models.TextField("Alergias")
    medicacoes= models.TextField("Medicações")
    patologias = models.TextField("Patologias")
    liquidos = models.TextField("Líquidos")
    alimentacao = models.TextField("Alimentação")
    elementos_relacionados = models.TextField("Elementos relacionados  (Alcool e outras drogas) ")
    data = models.DateTimeField(blank=True, null = True)
    profissional = models.TextField("Profissional")


class Acomp_farmacoterapico(models.Model):
    #basico
    num_pai = models.ForeignKey(Prontuario_de_Atendimento_Integral_PAI, on_delete = models.CASCADE)
    data_ini_acomp = models.DateTimeField(default=timezone.now(), blank = False, null = False)
    ALERGIAS = (
        ('Nega', "Nega"),
        ('Sim', "Sim"),
        ('Não sabe informar', "Não sabe informar"),
    )
    alergias = models.BooleanField()
    alergias_affirm = models.CharField("Alergias", max_length=255, choices = ALERGIAS, blank = True, null = True)

    def clean(self):
        if alergias:
            msg = forms.ValidationError("Este campo deve ser preenchido")
            self.add_error("alergias_affirm", msg)
        else:
            #mantem o banco de dados consistente a partir do erro
            #campo não selecionado
            self.cleaned_data['alergias_affirm'] = ''

    def publish(self):
        self.data_ini_acomp = timezone.now()
        self.save()