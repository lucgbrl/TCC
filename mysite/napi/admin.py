from django.contrib import admin
from .models import Prontuario_de_Atendimento_Integral_PAI, Seguimento_terapeutico
from .exchange import Acompanhamento_de_Pressao_Arterial_Glicemia, Requisicao_Exame_Citopatologico
from .ava import ava_clinica_med_sample

# Registrando os models provenientes do arquivo .models aqui
admin.site.register(Prontuario_de_Atendimento_Integral_PAI)
admin.site.register(Acompanhamento_de_Pressao_Arterial_Glicemia)
admin.site.register(Requisicao_Exame_Citopatologico)
admin.site.register(Seguimento_terapeutico)

# registrando arquivos provenientes do arquivos .exchange aqui
#admin.site.register(Acompanhamento_de_Pressao_Arterial_Glicemia)

#registrando modelos provenientes do arquivo ava.py aqui

admin.site.register(ava_clinica_med_sample)