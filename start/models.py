from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from shop.models import Produit
from blog.models import Article

#TODO : About us

class Taffich(models.Model):

    titre = models.CharField(max_length=255, null=True, blank=True)
    description = HTMLField('shop/descripion')
    cover = models.ImageField(upload_to='blog')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Advantage"
        verbose_name_plural = "Advantages"

    def __str__(self) -> str:
        return str(self.titre)
