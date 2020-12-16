from django.contrib import admin

from .models import Clientes,Veiculos, Locacao, Diaria

class clienteAdmin(admin.ModelAdmin):
    list_display = ('nomecompleto','idade','sexo')

class veiculosAdmin(admin.ModelAdmin):
    list_display = ('nome','anoveiculo','fabricante')

class locacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente','veiculo','datalocacao','datadevolucao')


admin.site.register(Clientes,clienteAdmin)
admin.site.register(Veiculos,veiculosAdmin)
admin.site.register(Locacao,locacaoAdmin)
admin.site.register(Diaria)
