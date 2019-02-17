from django.db import models
from django.utils import timezone

# Create your models here.
# Classes do projeto
class Prontuario_de_Atendimento_Integral_PAI(models.Model):

    numero_registro = models.CharField("Nº de registro", max_length=10)
    data_de_registro = models.DateTimeField(default=timezone.now)
    nome = text = models.TextField("Nome") 
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento"blank=True, null=True) 
    Idade = models.interger("Idade")
    Estado_Civil = models.text("Estado Civil")
    Nome_da_Mae = models.TextField("Nome da Mãe")
    Nome_do_Pai = models.TextField("Nome do Pai")
    Profissao = models.text("Profissão")
    Naturalidade = models.text("Naturalidade")
    Endereco = models.TextField("Endereço")
    Nº = models.interger("Nº")
    Bairro = models.text("Bairro")
    Cidade = models.text("Cidade")
    UF = models.text("UF")
    CEP = models.intergerFild("CEP"max_length=8)
    Etnia = models.text("Etnia")
    Sexo = models.text("Sexo")
    RG = intergerFild("RG"max_length=13)
    CPF = intergerFild("CPF"max_length=12)
    Cel = intergerFild("Celular"max_length=11)
    Fixo = intergerFild("Fixo"max_length=10)
    E-mail = models.text("E-mail")

    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()

class Ficha_de_Avaliação_Fisioterapia(models.Model):

        
    
