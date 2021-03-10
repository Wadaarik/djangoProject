from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'mail', 'titre', 'contenu') #Liste des champs a afficher
    search_fields = ('nom', 'mail') #Recherche par ces champs
    list_filter = ('nom', )

admin.site.register(Contact, ContactAdmin)