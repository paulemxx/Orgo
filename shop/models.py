# -*- coding: utf-8 -*-
from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet


# Create your models here.


class Tag(models.Model):
    titre = models.CharField(max_length=255, unique=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return str(self.titre)


class Categorie(models.Model):
    titre = models.CharField(max_length=255, unique=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return str(self.titre)



class Produit(models.Model):

    titre = models.CharField(max_length=50)
    titre_slug = models.SlugField(editable=False, null=True, max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = HTMLField('shop/description')
    old_prix = models.FloatField()
    new_prix = models.FloatField()


    cover = models.ImageField(upload_to='shop/images')


    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):

        return str(self.titre)

    def save(self, *args, **kwargs):
        super(Produit, self).save(*args, **kwargs)
        encoding_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(str(self.titre) + ' ' + str(encoding_id.hexdigest()))
        super(Produit, self).save(*args, **kwargs)


    @property
    def getReviews(self) -> QuerySet:
        return self.reviews.filter(statut=True).order_by('-date_add')


class Review(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='reviews')
    titre = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    review = models.TextField()

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:


        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):

        return self.titre

