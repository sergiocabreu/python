from django.shortcuts import render
from clientes.models import Clientes

def index(resquest):
	return render(resquest,'clientes_index.html', {'clientes_list' : Clientes.objects.all()})

def novo(request):
	return render(request,'cliente.html')	
