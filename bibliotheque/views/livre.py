from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http.request import HttpRequest
from django.shortcuts import render

from bibliotheque import models
from bibliotheque.forms import LivreForm, LivreNoCategorieForm


def bibliotheque_livre_all(request: HttpRequest):
    livres = models.Livre.objects.all()
    return render(request, "bibliotheque/livre/all.jinja", {"livres": livres})


def bibliotheque_livre(request: HttpRequest):
    return render(
        request,
        "bibliotheque/livre/add.jinja",
        {"livre": LivreForm()},
    )
    
def bibliotheque_livre_from_categorie(request: HttpRequest, id: int):
    return render(request, "bibliotheque/livre/addNoCategorie.jinja", {"livre": LivreNoCategorieForm(), "categorie_id": id})


def bibliotheque_livre_updateId(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound("Livre non trouvé.")

    return render(
        request,
        "bibliotheque/livre/update.jinja",
        {"livre": LivreForm(livre.__dict__), "id": livre.pk},
    )


def bibliotheque_api_livre(request: HttpRequest):
    form = LivreForm(request.POST)

    if form.is_valid():
        livre = form.save()
        return render(request, "bibliotheque/livre/add_success.jinja", {"livre": livre})
    else:
        return HttpResponseBadRequest(
            render(request, "bibliotheque/livre/add.jinja", {"livre": form})
        )

def bibliotheque_api_livre_fromcategorieId(request: HttpRequest, id: int):
    form = LivreForm(request.POST)
    categorie = models.Categorie.objects.get(pk=id)

    if form.is_valid():
        livre: models.Livre = form.save()
        livre.categorie = categorie
        livre.save()
        return render(request, "bibliotheque/livre/add_success.jinja", {"livre": livre})
    else:
        return HttpResponseBadRequest(
            render(request, "bibliotheque/livre/add.jinja", {"form": form})
        )


def bibliotheque_livreId(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound("Livre non trouvé.")

    return render(request, "bibliotheque/livre/read.jinja", {"livre": livre})


def bibliotheque_api_livre_updateId(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound("Livre non trouvé.")

    form = LivreForm(request.POST, instance=livre)

    if form.is_valid():
        livre = form.save()
        return render(request, "bibliotheque/livre/read.jinja", {"livre": livre})
    else:
        return HttpResponseBadRequest(
            render(request, "bibliotheque/livre/add.jinja", {"form": form})
        )


def bibliotheque_api_livre_deleteId(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound("Livre non trouvé.")

    livre_id = livre.pk
    livre.delete()
    return render(request, "bibliotheque/livre/delete_success.jinja", {"livre_id": livre_id})
