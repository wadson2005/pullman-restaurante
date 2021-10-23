from django.shortcuts import render
from .models import Dados_site, Produtos
def home(request):
    dados = Dados_site.objects.all()
    produtos = Produtos.objects.all()
    bd = {
        "dados": dados[0],
        "produtos": produtos
    }
    return render(request, "home.html", bd)