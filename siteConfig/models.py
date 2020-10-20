from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from shop.models import Produit
from blog.models import Article
from start.models import Call
from start.models import Mail
from start.models import Adresse
# TODO : Contact : Importation de start



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
