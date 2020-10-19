from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from siteConfig.datamanager import mergeData

from django.contrib.messages import constants as messages


# Create your views here.

def shop(request: HttpRequest) -> HttpResponse:
    data = {


        'prod': models.Produit.objects.filter(status=True).order_by('-date_add')[:3]

    }
    return render(request, 'pages/shop/shop.html', mergeData(request, data))


def product(request: HttpRequest, titre_slug: str) -> HttpResponse:
    data = {
        'single': models.Produit.objects.filter(status=True, titre_slug=titre_slug)[:1],
        'prod': models.Produit.objects.filter(status=True).order_by('-date_add')[:4],

    }
    return render(request, 'pages/shop/product.html', data)



