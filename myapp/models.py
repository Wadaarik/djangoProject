from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    nom = models.CharField(max_length=150)
    mail = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    contenu = models.TextField(max_length=200)