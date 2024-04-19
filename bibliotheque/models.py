from django.db import models

# Create your models here.


class Livre(models.Model):
    """Définition d'un livre, faisant part de la bibliothèque."""

    titre = models.CharField(max_length=100)

    auteur = models.CharField(max_length=100)

    date_publication = models.DateField(blank=True, null=True)

    nombre_pages = models.IntegerField(blank=False)

    resume = models.TextField(null=True, blank=True)

    categorie: models.ForeignKey["Categorie | None"] = models.ForeignKey(
        "Categorie", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.titre} écrit par {self.auteur} édité le {self.date_publication}"


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nom
