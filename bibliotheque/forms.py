from django.forms import ModelForm

from . import models


class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = [
            "titre",
            "auteur",
            "date_publication",
            "nombre_pages",
            "resume",
            "categorie",
        ]
        labels = {
            "titre": "Titre",
            "auteur": "Auteur",
            "date_publication": "Date de publication",
            "nombre_pages": "Nombre de pages",
            "resume": "Résumé",
            "categorie": "Catégorie",
        }
        
class LivreNoCategorieForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = [
            "titre",
            "auteur",
            "date_publication",
            "nombre_pages",
            "resume",
        ]
        labels = {
            "titre": "Titre",
            "auteur": "Auteur",
            "date_publication": "Date de publication",
            "nombre_pages": "Nombre de pages",
            "resume": "Résumé",
        }


class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ["nom", "description"]
        labels = {
            "nom": "Nom",
            "description": "Description",
        }
