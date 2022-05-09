from django.shortcuts import render, HttpResponseRedirect
from .forms import GameForm
from . import models

# Create your views here.

def index(request):
    return render(request, 'games/index.html')

def ajout(request):
    if request.method == "POST":
        form = GameForm(request)
        return render(request,"games/ajout.html",{'form' : form})
    else :
        form = GameForm()
        return render(request,"games/ajout.html", {"form" : form})

def traitement(request):
    gform = GameForm(request.POST)
    if gform.is_valid():
        game = gform.save()
        return HttpResponseRedirect("/games/liste")
    else :
        return render(request,"games/ajout.html", {"form" : gform})

def liste(request):
    liste = list(models.Game.objects.all())
    return render(request,"games/liste.html",{"liste" : liste})

def affiche(request, id):
    game = models.Game.objects.get(pk=id)
    return render(request,"games/affiche.html",{"game" : game})

def delete(request, id):
    game = models.Game.objects.get(pk=id)
    game.delete()
    return render(request, "games/delete.html",{"game" : game})

def update(request, id):
    game = models.Game.objects.get(pk=id)
    form = GameForm(game.dico)
    return render(request, "games/ajout.html",{"form": form, "id": id})

def updatetraitement(request, id):
    gform = GameForm(request.POST)
    if gform.is_valid():
        game = gform.save(commit=False)
        game.id = id
        game.save()
        return HttpResponseRedirect("/games/liste")
    else:
        return render(request, "games/ajout.html", {"form": gform, "id": id})
