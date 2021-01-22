from django.shortcuts import render, HttpResponse, redirect
from .models import Minigame

def index(request):
    if request.method == "POST":
        if request.POST.get("mg-read-more"):
            return None
    return render(request, "website/index.html")


def news(request):
    minigames = Minigame.objects.all()
    return render(request, "website/news.html", {"minigames": minigames})


def minigame(request):
    pass


def forum(request):
    return render(request, "website/forum.html")


def support(request):
    return render(request, "website/support.html")


def legal(request):
    return render(request, "website/legal.html")


def gallery(request):
    return render(request, "website/gallery.html")
