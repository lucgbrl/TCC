from django.db import models
from django.utils import timezone

# Create your models here.
# Classes do projeto
class Prontuario_de_Atendimento_Integral_PAI(models.Model):
    numero_registro = models.CharField("Nº de registro", max_length=10)
    data_de_registro = models.DateTimeField(default = timezone.now)
    nome = models.CharField("Nome", max_length = 64)
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento", blank = True, null = True)
    Idade = models.CharField("Idade", max_length=2)
    Estado_Civil = models.CharField("Estado Civil", max_length= 32)
    Nome_da_Mae = models.CharField("Nome da Mãe",  max_length= 64)
    Nome_do_Pai = models.CharField("Nome do Pai",  max_length= 64)
    Profissao = models.CharField("Profissão",  max_length= 32)
    Naturalidade = models.CharField("Naturalidade",  max_length= 32)
    Endereco = models.CharField("Endereço",  max_length= 32)
    N = models.IntegerField()
    Bairro = models.CharField("Bairro", max_length=32)
    Cidade = models.CharField("Cidade", max_length=32)
    UF = models.CharField(max_length=32)
    CEP = models.CharField(max_length=8)
    Etnia = models.CharField(max_length=32)
    Sexo = models.CharField(max_length=24)
    RG = models.CharField(max_length=11)
    CPF = models.CharField(max_length=11)
    Cel = models.CharField(max_length=11)
    Fixo = models.CharField(max_length=11)
    Email = models.CharField("E-mail", max_length=255)

    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()


class Seguimento_terapeutico(models.Model):
    numero_registro = models.ForeignKey(Prontuario_de_Atendimento_Integral_PAI, on_delete=models.CASCADE)
    conteudo = models.TextField()
    