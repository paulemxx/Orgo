from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# TODO : About us

class BackgroundAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'affiche_image'
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
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre',]}),
        ('Image', {'fields': ['cover', 'affiche_image', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class TaffichAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'description',
        'affiche_image'
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
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre', 'description', ]}),
        ('Image', {'fields': ['cover', 'affiche_image', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class QualityAdmin(admin.ModelAdmin):
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


class ChiffreAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'nombre',
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
        ('Info ', {'fields': ['titre', 'nombre']}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'description',
        'metier',
        'nom',
        'affiche_image'
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
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre', 'description', 'metier', 'nom',]}),
        ('Image', {'fields': ['cover', 'affiche_image', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class AvantageAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'recit',
        'nombre',
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
        ('Info ', {'fields': ['titre',  'recit', 'nombre',]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]

class TitleAdmin(admin.ModelAdmin):
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

# TODO : Teams

class TeamAdmin(admin.ModelAdmin):
    list_display = (

        'metier',
        'nom',
        'affiche_image'
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
        'nom',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['metier', 'nom',]}),
        ('Image', {'fields': ['cover', 'affiche_image', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]

# TODO : Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'titre',

        'affiche_image'
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
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre', ]}),
        ('Image', {'fields': ['cover', 'affiche_image', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]

# TODO : Faq

class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'questions',
        'reponses',

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
        ('Info ', {'fields': [ 'questions', 'reponses', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class FormfaqAdmin(admin.ModelAdmin):
    list_display = (
        'nom'
        'email',
        'sujet',
        'tel',
        'message',

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
        'nom',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['nom', 'email', 'sujet', 'tel', 'message',
]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]

# TODO : Services

class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'description',

        'affiche_image'
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
    readonly_fields = ['affiche_image']

    fieldsets = [
        ('Info ', {'fields': ['titre', 'description', ]}),
        ('Image', {'fields': ['cover', 'affiche_image', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]

# TODO : Contact

class AdresseAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'adress',

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
        ('Info ', {'fields': ['titre', 'adress', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class MailAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'email',

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
        ('Info ', {'fields': ['titre', 'email', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]


class CallAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'tel',

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
        ('Info ', {'fields': ['titre', 'tel', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]



def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Background, BackgroundAdmin)
_register(models.Taffich, TaffichAdmin)
_register(models.Quality, QualityAdmin)
_register(models.Chiffre,ChiffreAdmin)
_register(models.Avantage, AvantageAdmin)
_register(models.Title, TitleAdmin)
_register(models.Team, TeamAdmin)
_register(models.Gallery, GalleryAdmin)
_register(models.Faq, FaqAdmin)
_register(models.Formfaq, FormfaqAdmin)
_register(models.Services, ServicesAdmin)
_register(models.Adresse, AdresseAdmin)
_register(models.Mail, MailAdmin)
_register(models.Call, CallAdmin)



