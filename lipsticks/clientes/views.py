from django.shortcuts import render, redirect
from django.views.generic.base import View
from clientes.forms import ClientesForm
from clientes.models import Clientes

def index(resquest):
	return render(resquest,'clientes_index.html', {'clientes_list' : Clientes.objects.all()})

def novo(request):
	return render(request,'clientes.html')

class SalvarClientesView(View):

	template_name = 'clientes.html'
	def get(self, request, clientes_id):
		cliente = Clientes.objects.get(id=clientes_id)
		return render(request, self.template_name, {"cliente" : cliente})

	def post(self, request):
		form = ClientesForm(request.POST)
		dados_form = form.data

		id = dados_form['id']

		if id:
			cliente_editar = Clientes.objects.get(id=id)
			cliente_editar.nome = dados_form['nome']
			cliente_editar.contato = dados_form['contato']
			cliente_editar.save()
		else:
			cliente = Clientes(nome=dados_form['nome'],contato=dados_form['contato'])
			cliente.save()

		return redirect('clientes')
