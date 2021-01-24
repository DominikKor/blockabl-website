from django.shortcuts import render, HttpResponse, redirect
from .models import Minigame


def index(request):
    return render(request, "website/index.html")


def news(request):
    minigames = Minigame.objects.all()
    return render(request, "website/news.html", {"minigames": minigames})


def minigame(request, id):
    return render(request, "website/minigame.html", {"minigame": Minigame.objects.get(pk=id)})


def forum(request):
    return render(request, "website/forum.html")


def support(request):
    return render(request, "website/support.html")


def legal(request):
    return render(request, "website/legal.html")


def gallery(request):
    return render(request, "website/gallery.html")
