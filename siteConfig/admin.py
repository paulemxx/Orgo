from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

class LienAdmin(admin.ModelAdmin):
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

class DescriptifAdmin(admin.ModelAdmin):
    list_display = (
        'description',
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
        'description',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'

    fieldsets = [
        ('Info ', {'fields': ['description', ]}),
        ('Statut et Activations', {'fields': ['statut', ]}),
    ]




def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Lien, LienAdmin)
_register(models.Descriptif, DescriptifAdmin)



