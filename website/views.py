from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "website/index.html")


def news(request):
    return render(request, "website/news.html")


def forum(request):
    return render(request, "website/forum.html")


def support(request):
    return render(request, "website/support.html")


def legal(request):
    return render(request, "website/legal.html")


def gallery(request):
    return render(request, "website/gallery.html")
