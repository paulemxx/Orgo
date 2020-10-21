from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData

# Create your views here.

def blog(request: HttpRequest) -> HttpResponse:
    data = {

        'categories': models.Categorie.objects.filter(statut=True).order_by('-date_add'),


        'article': models.Article.objects.filter(statut=True)[:4],
        'articles': models.Article.objects.filter(statut=True),
        'tags': models.Tag.objects.filter(statut=True)[:5],

    }
    return render(request, 'pages/blog/blog.html', mergeData(request, data))


def single_blog(request: HttpRequest, titre_slug: str) -> HttpResponse:
    data = {

        'categories': models.Categorie.objects.filter(statut=True).order_by('-date_add'),

        'singles': models.Article.objects.filter(titre_slug=titre_slug)[:1],
        'tags': models.Tag.objects.filter(statut=True)[:5],
        'commentaires': models.Commentaire.objects.filter(statut=True).order_by('-date_add')[:6],

    }

    return render(request, 'pages/blog/single_blog.html', mergeData(request, data))





