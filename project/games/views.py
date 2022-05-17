from django.shortcuts import render, HttpResponseRedirect
from .forms import GameForm
from .forms import Catform
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

def ajout2(request):
    if request.method == "POST":
        form = Catform(request)
        return render(request,"games/ajout2.html",{'form' : form})
    else :
        form = Catform()
        return render(request,"games/ajout2.html", {"form" : form})

def traitement(request):
    gform = GameForm(request.POST)
    if gform.is_valid():
        game = gform.save()
        return HttpResponseRedirect("/games/liste")
    else :
        return render(request,"games/ajout.html", {"form" : gform})

def traitement2(request):
    cform = Catform(request.POST)
    if cform.is_valid():
        cat = cform.save()
        return HttpResponseRedirect("/games/liste2")
    else:
        return render(request, "games/ajout2.html", {"form": cform})

def liste(request):
    liste = list(models.Game.objects.all())
    return render(request,"games/liste.html",{"liste" : liste})

def liste2(request):
    liste = list(models.Categorie.objects.all())
    return render(request, "games/liste2.html", {"liste": liste})

def affiche(request, id):
    game = models.Game.objects.get(pk=id)
    return render(request,"games/affiche.html",{"game" : game})

def affiche2(request, id):
    cat = models.Categorie.objects.get(pk=id)
    return render(request, "games/affiche2.html", {"cat": cat})

def delete(request, id):
    game = models.Game.objects.get(pk=id)
    game.delete()
    return render(request, "games/delete.html",{"game" : game})

def delete2(request, id):
    cat = models.Categorie.objects.get(pk=id)
    cat.delete()
    return render(request, "games/delete2.html",{"cat" : cat})

def update(request, id):
    game = models.Game.objects.get(pk=id)
    form = GameForm(game.dico())
    return render(request, "games/ajout.html",{"form": form, "id": id})

def update2(request, id):
    cat = models.Categorie.objects.get(pk=id)
    form = Catform(cat.dico())
    return render(request, "games/ajout2.html", {"form": form, "id": id})

def updatetraitement(request, id):
    gform = GameForm(request.POST)
    if gform.is_valid():
        game = gform.save(commit=False)
        game.id = id
        game.save()
        return HttpResponseRedirect("/games/liste")
    else:
        return render(request, "games/ajout.html", {"form": gform, "id": id})

def updatetraitement2(request, id):
    cform = Catform(request.POST)
    if cform.is_valid():
        cat = cform.save(commit=False)
        cat.id = id
        cat.save()
        return HttpResponseRedirect("/games/liste2")
    else:
        return render(request, "games/ajout2.html", {"form": cform, "id": id})


