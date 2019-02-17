from django.contrib import admin
from .models import Prontuario_de_Atendimento_Integral_PAI
from .exchange import Acompanhamento_de_Pressao_Arterial_Glicemia

# Registrando os models provenientes do arquivo .models aqui
admin.site.register(Prontuario_de_Atendimento_Integral_PAI)

# registrando arquivos provenientes do arquivos .exchange aqui
admin.site.register(Acompanhamento_de_Pressao_Arterial_Glicemia)
