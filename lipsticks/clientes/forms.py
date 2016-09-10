from django import forms

class ClientesForm(forms.Form):
    nome = forms.CharField(required=True)
    contato = forms.CharField(required=True)