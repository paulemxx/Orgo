from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'status',
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
        ('Status et Activations', {'fields': ['status', ]}),
    ]


class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'status',
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
        ('Status et Activations', {'fields': ['status', ]}),
    ]


class ProduitAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'affiche_image',
        'affiche_image1',
        'affiche_image2',
        'affiche_image3',

        'categorie',
        'tag',
        'old_prix',
        'new_prix',
        'status',
        'date_add',
        'date_update'
    )
    list_filter = (
        'categorie',
        'status',
        'tag'
    )
    search_fields = (
        'titre',
    )
    list_per_pages = 50
    date_hierarchy = 'date_add'
    readonly_fields = ['affiche_image', 'affiche_image1', 'affiche_image2', 'affiche_image3', 'affiche_vid']

    fieldsets = [
        ('Info ', {'fields': [
            'titre',
            'categorie',
            'tag',
            'old_prix',
            'new_prix',
            'description',

        ]
        }),
        ('Image', {'fields': ['cover', 'affiche_image', 'img1', 'affiche_image1', 'img2', 'affiche_image2', 'img3',
                              'affiche_image3', 'video', 'affiche_vid', ]}),
        ('Status et Activations', {'fields': ['status', ]}),
    ]

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.cover.url))

    def affiche_image1(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.img1.url))

    def affiche_image2(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.img2.url))

    def affiche_image3(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.img3.url))

    def affiche_vid(self, obj):
        return mark_safe('<source src="{url}" width="100px" height="50px" />'.format(url=obj.video.url))


class ReviewAdmin(admin.ModelAdmin):


    list_display = ('name', 'status', 'date_add', 'date_update',)
    list_filter = ('name', 'status', 'date_add',)
    search_fields = ('name',)
    date_hierarchy = 'date_add'
    fieldsets = (
        ('Info', {
            'fields': [
                'name', 'email', 'review']

            ,
        }),
        ('Status et Activations', {'fields': ['status', ]}),
    )




def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Produit, ProduitAdmin)
_register(models.Review, ReviewAdmin)
_register(models.Tag, TagAdmin)
_register(models.Categorie, CategorieAdmin)