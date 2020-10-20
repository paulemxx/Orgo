from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from shop.models import Produit
from blog.models import Article


# TODO : Contact

class Adresse(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"


class Mail(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"


class Call(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    tel = models.CharField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Call"
        verbose_name_plural = "Calls"


# TODO : Liens

class Lien(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lien"
        verbose_name_plural = "Liens"

    def __str__(self) -> str:
        return str(self.titre)


class Descriptif(models.Model):
    description = models.TextField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Descriptif"
        verbose_name_plural = "Descriptifs"

    def __str__(self) -> str:
        return str(self.statut)
