from django.utils import timezone
from django.conf import settings
from django.db import models
from .models import Prontuario_de_Atendimento_Integral_PAI


class Acompanhamento_de_Pressao_Arterial_Glicemia(models.Model):
    num_pai = models.ForeignKey(Prontuario_de_Atendimento_Integral_PAI, on_delete = models.CASCADE)
    #cadastro de titulo
    cliente = models.CharField(max_length=200)

    #inteiros
    #pai = models.ForeignKey("PAI", 'Prontuario_de_Atendimento_Integral_PAI' , on_delete=models.CASCADE)

    #data e hora automatica
    data_de_solicitacao = models.DateTimeField(default=timezone.now)


    #cadastro de data do dia (campo do formulario)
    dia = models.DateTimeField(blank=True, null=True)

    #cadastro do turno e da hora (campo do formulario)
    turno = models.CharField(max_length = 20 ,)
    hora = models.DateTimeField(blank=True, null=True)

    #PA e Dx (Pressão e Glicemia)
    pa = models.CharField("PA", max_length = 20 ,  null = True, blank = True)
    dx = models.CharField("Dx", max_length = 20 ,  null = True, blank = True)

    #textos longos
    observacao = models.TextField("Observação", null = True, blank = True)

    #usuario que realiza o cadastro
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.dia = timezone.now()
        self.hora = timezone.now()
        self.save()

    def __str__(self):
        return self.cliente

class Requisicao_Exame_Citopatologico(models.Model):
    #basico
    num_pai = models.ForeignKey(Prontuario_de_Atendimento_Integral_PAI, on_delete = models.CASCADE)
    
    #dados redundantes, já presentes no formulário PAI
    nome_completo = models.CharField(max_length=200)
    Nome_da_Mae = models.CharField("Nome da Mãe", max_length=255)
    Data_de_Nascimento = models.DateTimeField("Data de nascimento", default = timezone.now)
    Idade = models.IntegerField("Idade")
    
    #endereço
    Rua = models.CharField("Endereço", max_length = 200)
    Nº = models.IntegerField("Nº")
    Bairro = models.CharField("Bairro", max_length = 200)
    Cidade = models.CharField("Cidade", max_length = 200 )
        
    #contatos
    Cel = models.IntegerField("Celular")
    #Fixo = models.IntegerField("Fixo")
    #email = models.CharField("E-mail", max_length = 200)

    #social
    RG = models.IntegerField("RG")
    CPF = models.IntegerField("CPF")
    
    ESCOLHA_CONFIRMA = (
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    )

    
    Rastreamento = models.CharField(max_length = 3, choices = ESCOLHA_CONFIRMA)
    Repeticao = models.CharField(max_length = 3, choices = ESCOLHA_CONFIRMA)
    Seguimento = models.CharField(max_length = 3, choices = ESCOLHA_CONFIRMA)
    Ultima_vez_que_papanicolau = models.TextField()
    
    Usa_anticoncep = models.BooleanField("Usa anticoncepcional?", default = False)
    Usa_Diu = models.BooleanField("Usa Diu?", default = False)
    Esta_gravida = models.BooleanField("Está grávida?", default = False)
    ultima_menstruacao = models.CharField("Última menstruação", max_length = 64, default = '', blank = True, null = True)
    sangramento_pos_relacao = models.BooleanField("Tem ou teve sangramento após relação?", default = False)
    Usa_hormonios = models.BooleanField("Usa hormônio?", default = False)

    #inspeção do colo
    normal = models.BooleanField("Colo normal?", default = False)
    anomalia_congen = models.BooleanField("Ausente anomalias congenitas ou retirada cirurgica", default = False)
    alterado = models.BooleanField("Alterado?", default = False)
    nao_visualizado = models.BooleanField("Colo não visualizado", null = True, blank = True, default = False)

    data = models.DateField(default = timezone.now, blank = True, null = True)

    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()
