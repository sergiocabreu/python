from django.db import models

class Clientes(models.Model):
	nome=models.CharField(max_length=200)
	contato=models.CharField(max_length=200)
