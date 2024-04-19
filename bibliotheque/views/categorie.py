from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http.request import HttpRequest
from django.shortcuts import render

from bibliotheque import models
from bibliotheque.forms import CategorieForm


def bibliotheque_categorie(request: HttpRequest):
    return render(request, "bibliotheque/categorie/add.jinja", {"categorie": CategorieForm()})


def bibliotheque_categorie_all(request: HttpRequest):
    return render(
        request, "bibliotheque/categorie/all.jinja", {"categories": models.Categorie.objects.all()}
    )


def bibliotheque_categorieId(request: HttpRequest, id: int):
    try:
        categorie = models.Categorie.objects.get(pk=id)
    except models.Categorie.DoesNotExist:
        return HttpResponseNotFound("Catégorie non trouvée.")

    return render(request, "bibliotheque/categorie/read.jinja", {"categorie": categorie})


def bibliotheque_api_categorie(request: HttpRequest):
    form = CategorieForm(request.POST)

    if form.is_valid():
        livre = form.save()
        return render(request, "bibliotheque/categorie/add_success.jinja", {"livre": livre})
    else:
        return HttpResponseBadRequest(
            render(request, "bibliotheque/categorie/add.jinja", {"categorie": form})
        )

def bibliotheque_categorie_updateId(request: HttpRequest, id: int):
    try:
        categorie = models.Categorie.objects.get(pk=id)
    except models.Categorie.DoesNotExist:
        return HttpResponseNotFound("Catégorie non trouvée.")
    
    return render(request, "bibliotheque/categorie/update.jinja", {"categorie": CategorieForm(categorie.__dict__), "categorie_id": categorie.pk})

def bibliotheque_api_categorie_updateId(request: HttpRequest, id: int):
    try:
        categorie = models.Categorie.objects.get(pk=id)
    except models.Categorie.DoesNotExist:
        return HttpResponseNotFound("Catégorie non trouvée.")

    form = CategorieForm(request.POST, instance=categorie)

    if form.is_valid():
        categorie = form.save()
        return render(request, "bibliotheque/categorie/read.jinja", {"categorie": categorie})
    else:
        return HttpResponseBadRequest(
            render(request, "bibliotheque/categorie/update.jinja", {"categorie": form, "id": id})
        )

def bibliotheque_api_categorie_deleteId(request: HttpRequest, id: int):
    try:
        categorie = models.Categorie.objects.get(pk=id)
    except models.Categorie.DoesNotExist:
        return HttpResponseNotFound("Catégorie non trouvée.")

    categorie_id = categorie.pk
    categorie.delete()
    return render(request, "bibliotheque/categorie/delete_success.jinja", {"categorie_id": categorie_id})
