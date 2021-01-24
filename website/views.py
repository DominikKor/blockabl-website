from django.shortcuts import render, HttpResponse, redirect
from .models import Gamemode


def index(request):
    return render(request, "website/index.html")


def news(request):
    return render(request, "website/news.html")


def gamemodes(request):
    all_gamemodes = Gamemode.objects.order_by("id")
    return render(request, "website/gamemodes.html", {"gamemodes": all_gamemodes})


def gamemode_detail(request, name):
    return render(request, "website/gamemode_detail.html", {"gamemode": Gamemode.objects.get(url=name)})


def forum(request):
    return render(request, "website/forum.html")


def support(request):
    return render(request, "website/support.html")


def legal(request):
    return render(request, "website/legal.html")


def gallery(request):
    return render(request, "website/gallery.html")
