from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from shop import models as shp_models
from siteConfig.datamanager import mergeData

# Create your views here.

def ajoutproduit(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':

        titre = request.POST.get('titre')
        categorie = request.POST.get('categorie')
        tag = request.POST.get('tag')
        old_prix = request.POST.get('old_prix')
        new_prix = request.POST.get('new_prix')
        resume = request.POST.get('resume')
        cover = request.FILES['cover']

        c = shp_models.Produit(


            titre=titre,
            categorie_id=int(categorie),
            tag_id=int(tag),
            old_prix=old_prix,
            new_prix=new_prix,
            resume=resume,
            cover=cover

        )

        c.save()
        return redirect('gestionadmin:index')
    else:
        data = {
            'categories': shp_models.Categorie.objects.filter(statut=True).order_by('-date_add'),
            'tags': shp_models.Tag.objects.filter(statut=True),
            'produits': shp_models.Produit.objects.filter(statut=True),

        }
        return render(request, 'pages/administration/shop/ajoutproduit.html', mergeData(request, data))

def ajoutcategorie(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        titre = request.POST.get('titre')

        c = shp_models.Categorie(

            titre=titre,

        )

        c.save()
        return redirect('gestionadmin:index')
    else:

        data = {
            'categories': shp_models.Categorie.objects.filter(statut=True).order_by('-date_add'),


        }
        return render(request, 'pages/administration/shop/ajoutcategorie.html', mergeData(request, data))


def ajouttag(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        titre = request.POST.get('titre')

        c = shp_models.Tag(

            titre=titre,

        )

        c.save()
        return redirect('gestionadmin:index')
    else:
        data = {
            'tags': shp_models.Tag.objects.filter(statut=True),

        }
        return render(request, 'pages/administration/shop/ajouttag.html', mergeData(request, data))



def listeproduit(request: HttpRequest) -> HttpResponse:
    data = {
        'prods': shp_models.Produit.objects.filter(statut=True).order_by('date_add'),

    }
    return render(request, 'pages/administration/shop/listeproduit.html', mergeData(request, data))



def listecategorie(request: HttpRequest) -> HttpResponse:
    data = {
        'categories': shp_models.Categorie.objects.filter(statut=True),


    }
    return render(request, 'pages/administration/shop/listecategorie.html', mergeData(request, data))



def listetag(request: HttpRequest) -> HttpResponse:
    data = {

        'tags': shp_models.Tag.objects.filter(statut=True),

    }
    return render(request, 'pages/administration/shop/listetag.html', mergeData(request, data))
