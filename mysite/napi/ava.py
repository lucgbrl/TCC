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
    data_ini_acomp = models.DateTimeField(default=timezone.now, blank = False, null = False)
    ALERGIAS = (
        ('Nega', "Nega"),
        ('Sim', "Sim"),
        ('Não sabe informar', "Não sabe informar"),
    )
    
    #alergias e coisas do tipo
    #o campo abaixo ativa um input field caso seja assinalado 'sim' para alergias
    alergias_affirm = models.CharField("Alergias", max_length=255, choices = ALERGIAS, blank = True, null = True)

    #comorbidades:
    diabetes = models.BooleanField("Diabetes", blank = True, null = True, default = False)
    hipertensao = models.BooleanField("Hipertensão", blank = True, null = True, default = False)
    outros = models.CharField("Outros", null = True, blank = True, max_length = 255)
    #motivacao
    motivacao = models.CharField("Motivo da busca por atendimento", blank = True, null = True, max_length = 255)
    problema_de_saude = models.TextField("Motivo da busca por atendimento", blank = True, null = True)
    
    def clean(self):
        if alergias:
            msg = forms.ValidationError("Este campo deve ser preenchido")
            self.add_error("alergias_affirm", msg)
        else:
            #mantem o banco de dados consistente a partir do erro
            #campo não selecionado
            self.cleaned_data['alergias_affirm'] = ''
        return self.cleaned_data

    def publish(self):
        self.data_ini_acomp = timezone.now()
        self.save()

class Ficha_ava_fisio(models.Model):
    #chaves estrangeiras devem preceder toda a estrutura da classe 
    num_pai = models.ForeignKey(Prontuario_de_Atendimento_Integral_PAI, on_delete = models.CASCADE)
    #info basica
    data_ini_acomp = models.DateField(default=timezone.now, blank = True, null = True)
    
    #lembrar de adicionar responsável
    hda = models.TextField("HDA", blank = True, null = True)
    hp = models.TextField("HP", blank = True, null = True)
    #exame fisico
    inspecao = models.TextField("Inspeção", blank = True, null = True)
    palpacao = models.TextField("Palpação", blank = True, null = True)
    adm = models.TextField("ADM", blank = True, null = True)
    #ava funcional
    ava_func = models.TextField("Capacidades funcionais", blank = True, null = True)
    asp_sens_cogn = models.TextField("Aspectos sensoriais e cognitivos", blank = True, null = True)
    lim_func = models.TextField("Limitações funcionais", blank = True, null = True)
    marcad_func = models.TextField("Marcador funcional", blank = True, null = True)

    def publish(self):
        self.data_ini_acomp = timezone.now()
        self.save()
        

class Param_laborais(models.Model):
    #referencia a Acomp_farmacoterapico
    referencia = models.ForeignKey(Acomp_farmacoterapico, on_delete = models.CASCADE)
    exame = models.CharField("Exames", max_length = 64)
    valor_de_referencia = models.CharField("Valores de referencia", max_length = 64)
    data1 = models.DateField(blank=True, null=True)
    data2 = models.DateField(blank=True, null=True)
    data3 = models.DateField(blank=True, null=True)
    data4 = models.DateField(blank=True, null=True)
    data5 = models.DateField(blank=True, null=True)

    def publish(self):
        self.data1 = timezone.now()
        self.data2 = timezone.now()
        self.data3 = timezone.now()
        self.data4 = timezone.now()
        self.data5 = timezone.now()
        self.save()