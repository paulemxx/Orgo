from django.shortcuts import redirect
from django.http.request import HttpRequest
from . import models


def getConfig(request: HttpRequest) -> dict:
    data = {

        'adresses': models.Adresse.objects.filter(statut=True).order_by('-date_add'),
        'calls': models.Call.objects.filter(statut=True).order_by('-date_add'),
        'mails': models.Mail.objects.filter(statut=True).order_by('-date_add'),

    }

    return data





def mergeData(request: HttpRequest, actual: dict) -> dict:
    actual.update(getConfig(request))
    return actual
