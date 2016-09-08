from django.db import models

class Compras(models.Model):
	nome_cliente = models.CharField(max_length=200)
	nome_produto = models.CharField(max_length=200)
