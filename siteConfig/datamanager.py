from django.shortcuts import redirect
from django.http.request import HttpRequest
from . import models


def getConfig(request: HttpRequest) -> dict:
    data = {

    }

    return data





def mergeData(request: HttpRequest, actual: dict) -> dict:
    actual.update(getConfig(request))
    return actual
