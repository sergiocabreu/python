from django.conf.urls import url, include
from django.contrib import admin
from compras import views as compras_views

urlpatterns = [
    url(r'^$', compras_views.index, name='index'),
    url(r'^compras/salvar$', compras_views.SalvarContaView.as_view(), name='compras_salvar'),
    url(r'^compras/salvar/(?P<compras_id>\d+)$', compras_views.SalvarContaView.as_view(), name='compras_editar')
]
