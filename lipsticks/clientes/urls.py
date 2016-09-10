from django.conf.urls import url, include
from clientes import views as clientes_view

urlpatterns = [
    url(r'^clientes$', clientes_view.index, name='clientes'),
    url(r'^clientes/salvar$', clientes_view.SalvarClientesView.as_view(), name='clientes_salvar'),
    url(r'^clientes/salvar/(?P<clientes_id>\d+)$', clientes_view.SalvarClientesView.as_view(), name='clientes_editar'),
    url(r'^clientes/novo$', clientes_view.novo, name='clientes_novo')
]
