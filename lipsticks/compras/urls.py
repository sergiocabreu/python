from django.conf.urls import url, include
from django.contrib import admin
from compras import views as compras_views

urlpatterns = [
    url(r'^$', compras_views.index, name='index'),
    url(r'^compras/$', compras_views.compras, name='compras')
]
