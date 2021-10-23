from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Dados_site, Produtos

#admin.site.register(Dados_site)
@admin.register(Dados_site)
class Dados_siteadmin(admin.ModelAdmin):
    list_display = ["nome", "telefone", "orário_funcionamento"]
admin.site.register(Produtos)