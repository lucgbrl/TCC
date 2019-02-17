from django.db import models
from django.utils import timezone

# Create your models here.
# Classes do projeto
class Prontuario_de_Atendimento_Integral_PAI(models.Model):

    numero_registro = models.CharField("Nº de registro", max_length=10)
    data_de_registro = models.DateTimeField(default=timezone.now)
    nome = text = models.TextField("Nome") 
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento"blank=True, null=True) 
    Idade = models.Interger("Idade")
    Estado_Civil = models.Text("Estado Civil")
    Nome_da_Mae = models.TextField("Nome da Mãe")
    Nome_do_Pai = models.TextField("Nome do Pai")
    Profissao = models.Text("Profissão")
    Naturalidade = models.Text("Naturalidade")
    Endereco = models.TextField("Endereço")
    Nº = models.Interger("Nº")
    Bairro = models.Text("Bairro")
    Cidade = models.Text("Cidade")
    UF = models.Text("UF")
    CEP = models.IntergerFild("CEP")
    Etnia = models.Text("Etnia")
    Sexo = models.Text("Sexo")
    RG = models.IntergerFild("RG")
    CPF = models.IntergerFild("CPF")
    Cel = models.IntergerFild("Celular")
    Fixo = models.IntergerFild("Fixo")
    Email = models.Text("E-mail")

    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()

class Ficha_de_Avaliação_Fisioterapia(models.Model):
#teste
#teste
    Data = models.DateTimeField("Data"default=timezone.now)  
    Telefone = intergerFild("Telefone"max_length=10)

    #Dados_Pessoais
    Nome = models.TextField("Nome")
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento"blank=True, null=True)
    Idade = models.Interger("Idade")
    Responsavel = models.Text("Responsável")
    HDA = models.TextField("HDA")
    HP = models.TextField("HP")
    
    #Exame_Físico
    Inspecao = models.TextField("Inspeção")
    Palpacao = models.TextField("Palpação")
    ADM = models.TextField("ADM")

    #Avaliação Funcional
    Capacidades_Funcionais models.TextField("Capacidades Funcionais")
    Aspectos_Sensorias_e_Cognitivos models.TextField("Aspectos Sensoriais e Cognitivos")
    Limitacoes_Funcionais models.TextField("Limitações Funcionais")
    Marcador_Funcional models.TextField("Marcador Funcional")

    Assinatura_do_Profissional = models.Text("Assinatura do Profissional")


    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()
