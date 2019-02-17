from django.db import models
from django.utils import timezone

# Create your models here.
# Classes do projeto
class Prontuario_de_Atendimento_Integral_PAI(models.Model):

    numero_registro = models.CharField("Nº de registro", max_length=10)
    data_de_registro = models.DateTimeField(default = timezone.now)
    #nome_pront = text = models.TextField("Nome") 
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento", blank=True, null=True) 
    Idade = models.IntegerField("Idade")
    Estado_Civil = models.TextField("Estado Civil")
    Nome_da_Mae = models.TextField("Nome da Mãe")
    Nome_do_Pai = models.TextField("Nome do Pai")
    Profissao = models.TextField("Profissão")
    Naturalidade = models.TextField("Naturalidade")
    Endereco = models.TextField("Endereço")
    Nº = models.IntegerField("Nº")
    Bairro = models.TextField("Bairro")
    Cidade = models.TextField("Cidade")
    UF = models.TextField("UF")
    CEP = models.IntegerField("CEP")
    Etnia = models.TextField("Etnia")
    Sexo = models.TextField("Sexo")
    RG = models.IntegerField("RG")
    CPF = models.IntegerField("CPF")
    Cel = models.IntegerField("Celular")
    Fixo = models.IntegerField("Fixo")
    email = models.CharField("E-mail", max_length = 200)

    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()

class Ficha_de_Avaliação_Fisioterapia(models.Model):

    Data = models.DateTimeField("Data" , default=timezone.now)  
    Telefone = models.CharField("Telefone" , max_length=10)

    #Dados_Pessoais
    nome = models.TextField("Nome")
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento", blank=True , null=True)
    Idade = models.IntegerField("Idade")
    Responsavel = models.TextField("Responsável")
    HDA = models.TextField("HDA")
    HP = models.TextField("HP")
    
    #Exame_Físico
    Inspecao = models.TextField("Inspeção")
    Palpacao = models.TextField("Palpação")
    ADM = models.TextField("ADM")

    #Avaliação Funcional
    Capacidades_Funcionais = models.TextField("Capacidades Funcionais")
    Aspectos_Sensorias_e_Cognitivos = models.TextField("Aspectos Sensoriais e Cognitivos")
    Limitacoes_Funcionais = models.TextField("Limitações Funcionais")
    Marcador_Funcional  = models.TextField("Marcador Funcional")

    Assinatura_do_Profissional = models.TextField("Assinatura do Profissional")


    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()
