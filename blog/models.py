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

    @property
    def getArticles(self) -> QuerySet:
        return self.articles.filter(statut=True)


class Article(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='useart')
    tags = models.ManyToManyField(Tag, related_name='articls')
    titre = models.CharField(max_length=50)
    titre_slug = models.SlugField(editable=False, null=True, max_length=255)
    cover = models.ImageField(upload_to='articles')
    contenu = HTMLField('Content')
    resume = HTMLField('Content')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='articles')


    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self) -> str:
        return str(self.titre)

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        encoding_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(str(self.titre) + ' ' + str(encoding_id.hexdigest()))
        super(Article, self).save(*args, **kwargs)

    @property
    def getCategories(self) -> QuerySet:
        return self.categories.filter(statut=True)

    @property
    def getTags(self) -> QuerySet:
        return self.tags.filter(statut=True)

    @property
    def getCommentaires(self) -> QuerySet:
        return self.commentaires.filter(statut=True).order_by('-date_add')

    @property
    def countCommentaires(self):
        return self.getCommentaires.count()


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    cover = models.ImageField(upload_to='blog')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self) -> str:
        return '{}  -  {}'.format(self.nom, self.date_add)

