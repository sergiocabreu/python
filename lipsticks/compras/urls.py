from django.conf.urls import url, include
from compras import views as compras_view

urlpatterns = [
    url(r'^$', compras_view.index, name='index'),
    url(r'^compras/salvar$', compras_view.SalvarContaView.as_view(), name='compras_salvar'),
    url(r'^compras/salvar/(?P<compras_id>\d+)$', compras_view.SalvarContaView.as_view(), name='compras_editar'),
    url(r'^compras/novo$', compras_view.novo, name='compras_novo')
]
