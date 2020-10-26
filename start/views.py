from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':

        email = request.POST.get('email')

        c = models.Newsletter(


            email=email,


        )

        c.save()
        return redirect('start:index')
    else:

        data = {
            'prods': models.Produit.objects.filter(statut=True).order_by('-date_add')[:4],
            'articles': models.Article.objects.filter(statut=True),
            'prod': models.Produit.objects.filter(statut=True).order_by('date_add')[:4],
            'news': models.Newsletter.objects.filter(statut=True),

            'sponsors': models.Sponsor.objects.filter(statut=True),


        }
        return render(request, 'pages/index.html', mergeData(request, data))



def about(request: HttpRequest) -> HttpResponse:
    data = {
        'backs': models.Background.objects.filter(statut=True).order_by('-date_add'),
        'affs': models.Taffich.objects.filter(statut=True).order_by('-date_add'),
        'qualitys': models.Quality.objects.filter(statut=True).order_by('-date_add'),
        'chiffres': models.Chiffre.objects.filter(statut=True).order_by('-date_add'),
        'avantages': models.Avantage.objects.filter(statut=True).order_by('-date_add'),
        'titles': models.Title.objects.filter(statut=True).order_by('-date_add'),
        'teams': models.Team.objects.filter(statut=True).order_by('-date_add'),

    }
    return render(request, 'pages/about.html', mergeData(request, data))



def gallery(request: HttpRequest) -> HttpResponse:

    data = {
        'gallerys': models.Gallery.objects.filter(statut=True).order_by('-date_add'),

    }
    return render(request, 'pages/gallery.html',mergeData(request, data))


def faq(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        c = models.Formfaq(

            nom=nom,
            email=email,
            tel=tel,
            sujet=sujet,
            message=message,

        )

        c.save()
        return redirect('start:index')
    else:
        data = {
            'faqs': models.Faq.objects.filter(statut=True).order_by('-date_add'),
            'formfaqs': models.Formfaq.objects.filter(statut=True).order_by('-date_add'),

        }
    return render(request, 'pages/faq.html', mergeData(request, data))



def team(request: HttpRequest) -> HttpResponse:
    data = {
        'teams': models.Team.objects.filter(statut=True).order_by('-date_add'),

    }
    return render(request, 'pages/team.html', mergeData(request, data))



def services(request: HttpRequest) -> HttpResponse:
    data = {
        'services': models.Services.objects.filter(statut=True).order_by('-date_add'),

    }
    return render(request, 'pages/services.html', mergeData(request, data))


def contact(request: HttpRequest) -> HttpResponse:
    data = {
        'adresses': models.Adresse.objects.filter(statut=True).order_by('-date_add'),
        'calls': models.Call.objects.filter(statut=True).order_by('-date_add'),
        'mails': models.Mail.objects.filter(statut=True).order_by('-date_add'),


    }
    return render(request, 'pages/contact.html', mergeData(request, data))



