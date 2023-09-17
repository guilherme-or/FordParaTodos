from django.contrib import admin
from .models import Usuario, Cor, Carro, Personalizacao, Solicitacao

admin.site.register(Usuario)
admin.site.register(Cor)
admin.site.register(Carro)
admin.site.register(Personalizacao)
admin.site.register(Solicitacao)
