from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [

    path('ajoutproduit', views.ajoutproduit, name='ajoutproduit'),
    path('ajoutcategorie', views.ajoutcategorie, name='ajoutcategorie'),
    path('ajouttag', views.ajouttag, name='ajouttag'),
    path('listeproduit', views.listeproduit, name='listeproduit'),
    path('listecategorie', views.listecategorie, name='listecategorie'),
    path('listetag', views.listetag, name='listetag'),

]