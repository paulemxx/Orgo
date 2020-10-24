from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from blog import models as blg_models
from siteConfig.datamanager import mergeData


# Create your views here.

def ajoutarticle(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        auteur = request.POST.get('auteur')
        titre = request.POST.get('titre')
        categorie = request.POST.get('categorie')
        tag = request.POST.get('tag')
        contenu = request.POST.get('contenu')
        resume = request.POST.get('resume')
        cover = request.FILES['cover']

        c = blg_models.Article(

            auteur=auteur,
            titre=titre,
            categorie=categorie,
            tag = tag,
            contenu=contenu,
            resume=resume,
            cover=cover

        )

        c.save()
        return redirect('shop:index')
    else:
        data = {

        }
        return render(request, 'pages/administration/blog/ajoutarticle.html', mergeData(request, data))


def ajoutcategorie(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        titre = request.POST.get('titre')

        c = blg_models.Categorie(

            titre=titre,

        )

        c.save()
        return redirect('gestionadmin:index')
    else:

        data = {

        }
        return render(request, 'pages/administration/blog/ajoutcategorie.html', mergeData(request, data))


def ajouttag(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        titre = request.POST.get('titre')

        c = blg_models.Tag(

            titre=titre,

        )

        c.save()
        return redirect('gestionadmin:index')
    else:
        data = {

        }
        return render(request, 'pages/administration/blog/ajouttag.html', mergeData(request, data))


def listearticle(request: HttpRequest) -> HttpResponse:
    data = {

        'articles': blg_models.Article.objects.filter(statut=True),

    }
    return render(request, 'pages/administration/blog/listearticle.html', mergeData(request, data))


def listecategorie(request: HttpRequest) -> HttpResponse:
    data = {
        'categories': blg_models.Categorie.objects.filter(statut=True).order_by('-date_add'),

    }
    return render(request, 'pages/administration/blog/listecategorie.html', mergeData(request, data))


def listetag(request: HttpRequest) -> HttpResponse:
    data = {

        'tags': blg_models.Tag.objects.filter(statut=True),

    }
    return render(request, 'pages/administration/blog/listetag.html', mergeData(request, data))
