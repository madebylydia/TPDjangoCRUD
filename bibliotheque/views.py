from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
from django.http.request import HttpRequest

from bibliotheque import models
from bibliotheque.forms import LivreForm

# Create your views here.


def front_all_livres(request: HttpRequest):
    livres = models.Livre.objects.all()
    return render(request, 'bibliotheque/all.jinja', {'livres': livres})

def front_creation_livre(request: HttpRequest):
    return render(request, 'bibliotheque/ajout.jinja', {'form': LivreForm()})

def front_update_livre(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound('Livre non trouvé.')

    return render(request, 'bibliotheque/update.jinja', {'livre': LivreForm(livre.__dict__), 'id': livre.pk})

def crud_livre_create(request: HttpRequest):
    form = LivreForm(request.POST)

    if form.is_valid():
        livre = form.save()
        return render(request, 'bibliotheque/ajout_success.jinja', {'livre': livre})
    else:
        return HttpResponseBadRequest(render(request, 'bibliotheque/ajout.jinja', {'form': form}))

def crud_livre_read(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound('Livre non trouvé.')

    return render(request, 'bibliotheque/affiche.jinja', {'livre': livre})


def crud_livre_update(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound('Livre non trouvé.')

    form = LivreForm(request.POST, instance=livre)

    if form.is_valid():
        livre = form.save()
        return render(request, 'bibliotheque/affiche.jinja', {'livre': livre})
    else:
        return HttpResponseBadRequest(render(request, 'bibliotheque/ajout.jinja', {'form': form}))

def crud_livre_delete(request: HttpRequest, id: int):
    try:
        livre = models.Livre.objects.get(pk=id)
    except models.Livre.DoesNotExist:
        return HttpResponseNotFound('Livre non trouvé.')
    livre_id = livre.pk
    livre.delete()
    return render(request, 'bibliotheque/delete_success.jinja', {'livre_id': livre_id})
