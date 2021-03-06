from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from siteConfig.datamanager import mergeData
from django.contrib.messages import constants as messages
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.
from .models import Produit, Cart


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

            produit_id=produit_id,
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


def cart(request: HttpRequest) -> HttpResponse:
    data = {

        'cart': models.Cart.objects.filter(statut=True),
        'product': models.Produit.objects.filter(statut=True).order_by('date_add'),

    }
    return render(request, 'pages/shop/cart.html', mergeData(request, data))


@login_required(login_url='shop:index')
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produit, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('shop:cart')


@login_required(login_url='shop:index')
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produit, id=product_id)
    cart.remove(product)
    return redirect('shop:cart')
