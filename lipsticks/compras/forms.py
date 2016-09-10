from django import forms

class ComprasForm(forms.Form):
	nome_cliente = forms.CharField(required=True)
	nome_produto = forms.CharField(required=True)