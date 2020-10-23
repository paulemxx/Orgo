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


        'prod': models.Produit.objects.filter(statut=True).order_by('-date_add')

    }
    return render(request, 'pages/shop/shop.html', mergeData(request, data))


def product(request: HttpRequest, titre_slug: str) -> HttpResponse:
    if request.method == 'POST':
        produit_id = request.POST.get('produit')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        titre = request.POST.get('titre')
        review = request.POST.get('review')

        c = models.Review(

            produit_id = produit_id,
            nom=nom,
            email=email,
            titre=titre,
            review=review,


        )

        c.save()
        return redirect('shop:index')
    else:
        data = {
            'singles': models.Produit.objects.filter(statut=True, titre_slug=titre_slug)[:1],
            'prod': models.Produit.objects.filter(statut=True).order_by('-date_add')[:3],
            'tags': models.Tag.objects.filter(statut=True)[:5],
            'prods': models.Produit.objects.filter(statut=True).order_by('date_add')[:3],


        }
        return render(request, 'pages/shop/shop_details.html', data)



