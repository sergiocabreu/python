from django.shortcuts import render, redirect
from django.views.generic.base import View
from compras.forms import ComprasForm
from compras.models import Compras

def index(request):
	return render(request,'index.html', {'compras_list': Compras.objects.all()})

def novo(request):
	return render(request,'compras.html')	

class SalvarContaView(View):	
	template_name = 'compras.html'

	def get(self, request, compras_id):
		compra = Compras.objects.get(id=compras_id)
		return render(request, self.template_name, {'compra' : compra})
		
	def post(self, request):
		form = ComprasForm(request.POST)
		dados_form = form.data

		id = dados_form['id']

		if id :
			compras_para_atualizar = Compras.objects.get(id=id)
			compras_para_atualizar.nome_cliente = dados_form['nome_cliente']
			compras_para_atualizar.nome_produto = dados_form['nome_produto']
			compras_para_atualizar.save()
		else:
			compra = Compras(nome_cliente=dados_form['nome_cliente'], nome_produto=dados_form['nome_produto'])
			compra.save()
	
		return redirect('index')
