# -*- coding: utf-8 -*-
from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from shop.models import Produit
from blog.models import Article


# TODO : About us

class Background(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    cover = models.ImageField(upload_to='back')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Background"
        verbose_name_plural = "Background"

    def __str__(self) -> str:
        return str(self.titre)


class Taffich(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    description = HTMLField('shop/descripion')
    cover = models.ImageField(upload_to='blog')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Taffich"
        verbose_name_plural = "Taffichs"

    def __str__(self) -> str:
        return str(self.titre)


class Quality(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Quality"
        verbose_name_plural = "Quality"

    def __str__(self) -> str:
        return str(self.titre)


class Chiffre(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)

    nombre = models.IntegerField()
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chiffre"
        verbose_name_plural = "Chiffres"

    def __str__(self) -> str:
        return str(self.titre)


class Feedback(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    description = HTMLField('start/description')
    metier = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    cover = models.ImageField(upload_to='start')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacky"

    def __str__(self) -> str:
        return str(self.titre)


class Avantage(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    recit = models.CharField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Avantage"
        verbose_name_plural = "Avantages"

    def __str__(self) -> str:
        return str(self.titre)


class Title(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = "Title"

    def __str__(self) -> str:
        return str(self.titre)


# TODO : Teams

class Team(models.Model):
    metier = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    cover = models.ImageField(upload_to='start')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self) -> str:
        return str(self.metier)


# TODO : Gallery

class Gallery(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    cover = models.ImageField(upload_to='start')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

    def __str__(self) -> str:
        return str(self.titre)


# TODO : Faq

class Faq(models.Model):
    questions = models.CharField(max_length=255, null=True, blank=True)
    reponses = models.CharField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Faq"
        verbose_name_plural = "Faqs"

    def __str__(self) -> str:
        return str(self.statut)


class Formfaq(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    sujet = models.CharField(max_length=255, null=True, blank=True)
    tel = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Formfaq"
        verbose_name_plural = "Formfaqs"

    def __str__(self) -> str:
        return str(self.nom)


# TODO : Services

class Services(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    description = HTMLField('start/description')
    cover = models.ImageField(upload_to='start/services')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"

    def __str__(self) -> str:
        return str(self.titre)


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

class Newsletter(models.Model):
    email = models.EmailField(max_length=255, null=True, blank=True)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self) -> str:
        return str(self.email)

class Sponsor(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    cover = models.ImageField(upload_to='start/services')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"

    def __str__(self) -> str:
        return str(self.titre)