from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'statut',
        'date_add',
        'date_update'
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['titre', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'statut',
        'date_add',
        'date_update'
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['titre', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class CommentaireAdmin(admin.ModelAdmin):

    def affiche_image(self, obj):
        if obj.cover:
            return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))

    list_display = (
        'article',
        'nom',
        'email',
        'message',
        'affiche_image',
        'statut',
        'date_add',
        'date_update'
    )

    list_filter = (
        'article',
        'statut',
        'date_add',
        'date_update'
    )
    search_fields = (
        'message',
        'date_add'
    )
    readonly_fields = ['affiche_image']
    fieldsets = [
        ('Info ', {'fields': ['article', 'nom', 'email', 'message', ]
        }),
        ('Image', {'fields': [
            'cover',
            'affiche_image'
        ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'auteur',
        'titre',
        'affiche_image',
        'statut',
        'date_add',
        'date_update'
    )
    list_filter = (
        'categorie',
        'statut',
        'tags'
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': [
            'auteur',
            'titre',
            'categorie',
            'tags',
            'contenu',
            'resume'
        ]
        }),
        ('Image', {'fields': ['cover', 'affiche_image']}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))








def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)


