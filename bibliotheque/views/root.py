from django.http import HttpRequest
from django.shortcuts import render

from bibliotheque.forms import CategorieForm, LivreForm


def bibliotheque(request: HttpRequest):
    return render(
        request,
        "bibliotheque/hello.jinja",
        {"form_livre": LivreForm(), "form_categorie": CategorieForm()},
    )
