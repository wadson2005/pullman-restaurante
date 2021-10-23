from django.db import models

class Dados_site(models.Model):
    nome = models.CharField("Nombre", max_length=50)
    telefone = models.CharField("Telefono", max_length=20)
    localizacao = models.TextField("localizacion")
    whatsapp = models.TextField("whatsapp")
    slogan = models.CharField("slogan", max_length=200)
    orário_funcionamento = models.CharField("Orário", max_length=100)
    email = models.CharField("correo electronico", max_length=100)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome_produto = models.CharField("Nombre del producto", max_length=20)
    descricao = models.TextField("descripcion")
    preco = models.DecimalField("precio", max_digits=7, decimal_places=2)
    link_imagem = models.TextField("texto", null=True, blank=True)

    def __str__(self):
        return self.nome_produto