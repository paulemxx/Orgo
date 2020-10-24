from django.urls import path
from gestionadmin.shops import views

app_name = 'shops'

urlpatterns = [

    path('ajoutproduit', views.ajoutproduit, name='ajoutproduit'),
    path('ajoutcategorie', views.ajoutcategorie, name='ajoutcategorie'),
    path('ajouttag', views.ajouttag, name='ajouttag'),
    path('listeproduit', views.listeproduit, name='listeproduit'),
    path('listecategorie', views.listecategorie, name='listecategorie'),
    path('listetag', views.listetag, name='listetag'),

]