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
    Nome_do_Pai = models.TextField("Nome do Pai",  max_length= 64)
    Profissao = models.TextField("Profissão",  max_length= 32)
    Naturalidade = models.TextField("Naturalidade",  max_length= 32)
    Endereco = models.CharField("Endereço",  max_length= 32)
    N = models.IntegerField()
    Bairro = models.CharField("Bairro", max_length=32)
    Cidade = models.CharField("Cidade", max_length=32)
    UF = models.TextField()
    CEP = models.CharField(max_length=8)
    Etnia = models.TextField()
    Sexo = models.TextField()
    RG = models.CharField(max_length=11)
    CPF = models.CharField(max_length=11)
    Cel = models.CharField(max_length=11)
    Fixo = models.CharField(max_length=11)
    Email = models.TextField("E-mail")

    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()

"""
class Ficha_de_Avaliação_Fisioterapia(models.Model):
    # teste
    # teste
    Data = models.DateTimeField("Data"
    default = timezone.now)
    Telefone = intergerFild("Telefone"
    max_length = 10)

    # Dados_Pessoais
    Nome = models.TextField("Nome")
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento"
    blank = True, null = True)
    Idade = models.Interger("Idade")
    Responsavel = models.Text("Responsável")
    HDA = models.TextField("HDA")
    HP = models.TextField("HP")

    # Exame_Físico
    Inspecao = models.TextField("Inspeção")
    Palpacao = models.TextField("Palpação")
    ADM = models.TextField("ADM")

    # Avaliação Funcional
    Capacidades_Funcionais
    models.TextField("Capacidades Funcionais")
    Aspectos_Sensorias_e_Cognitivos
    models.TextField("Aspectos Sensoriais e Cognitivos")
    Limitacoes_Funcionais
    models.TextField("Limitações Funcionais")
    Marcador_Funcional
    models.TextField("Marcador Funcional")

    Assinatura_do_Profissional = models.Text("Assinatura do Profissional")

    def publish(self):
        self.Data_de_Nascimento = timezone.now()
        self.save()


class Avaliacao_Clinica(models.Model):
    Data = models.DateTimeField(default=timezone.now)

    # Medidas
    Peso = models.IntergerFild("Peso")
    Altura = models.IntergerFild("Altura")
    Tipo_Sanguineo = models.TextField("Tipo_Sanquíneo")
    P_A = models.IntergerFild("P.A")
    D_X = models.IntergerFild("D.X")
    F_R = models.IntergerFild("F.R")
    Pulso = models.IntergerFild("Pulso")
    Glicemia = models.IntergerFild("Pulso")
    IMC = models.IntergerFild("IMC")
    Perimetro_Cefalico = models.TextField("Perímetro Cefálico")

    # Sampla
    Sinais_e_Sintomas = models.TextField("Sinais e Sintomas")
    Alergias = models.TextField("Alergias")
    Medicacoes = models.TextField("Medicações")
    Patologias = models.TextField("Patologias")
    Liquidos = models.TextField("Líquidos")
    Alimentoacao = models.TextField("Alimentação")
    Elementos_Relacionados = models.TextField("Elementos Relacionados(Alcool e Outras Drogas")
    Data = models.DateTimeField("Data"
    default = timezone.now)
    Profissional = models.TextField("Profissional")

    def publish(self):
        self.Data = timezone.now()
        self.save()


class Seguimento_Terapeutico(models.Model):
    Seguimento_Terapeutico = models.TextField("Seguimento Terapêutico")


class Ficha_de_Atendimento_Nutricao(models.Model):
    Data = models.DateTimeField("Data de Nascimento"
    blank = True, null = True)
    # 1_Identificação

    Nome_Completo = models.TextField("Nome Completo")
    Data_de_Nascimento = models.DateTimeField("Data de Nascimento"
    blank = True, null = True)
    Idade = models.IntergerFild("Idade")
    Cidade = models.TextField("Cidade")
    Email = models.TextField("E-mail")

    Por_que_voce_procurou_o_atendimento_nutricional = models.TextField(
        "Por_que_voce_procurou_o_atendimento_nutricional?")

    #Tem_algumas_das_patologias_abaixo()

    Problemas_Cardiacos = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Hipertensao = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Colesterol_elevado = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Convulsoes = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Dor_de_cabeca_frequente = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Constipacao / dias = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Problemas_pulmonares = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Bronquite = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Glicose_elevada = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Fratura_ossea = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Empachamento = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    EH = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Tonturas = models.CharField(max_length=3, choices = ESCOLHA_CONFIRMA)
    Asma = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Diabetes = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Cirugia = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Azia = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)
    Gastrite = models.CharField(max_length=3, choices=ESCOLHA_CONFIRMA)

    Outros = models.TextField("Outros")
    HPP = models.TextField("HPP")

    Voce_faz_uso_de_algum_medicamento = (
        ('SIM', 'Sim'),
        ('NAO', 'Não')
    )

    Voce_usa_medicamento = models.CharField(max_lenth=3, choices=Voce_faz_uso_de_algum_medicamento)

    Medicamento = models.CharField("Medicamento", max_length=200)
    Horario = models.DataTimeFild("Horário", blank=True, null=True)

    def publish(self):
        self.Data = timezone.now()
        self.save()
"""