from django.urls import path
from website import views

urlpatterns = [
    path("", views.index, name="index"),
    path("news/", views.news, name="news"),
    path("forum/", views.forum, name="forum"),
    path("support/", views.support, name="support"),
    path("legal/", views.legal, name="legal"),
    path("gallery/", views.gallery, name="gallery"),
]