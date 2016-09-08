from django import forms
from django.contrib.auth.models import User

class ComprasForm(forms.Form):

	nome_cliente = forms.CharField(required=True)
	nome_produto = forms.CharField(required=True)