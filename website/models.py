from django.db import models


class Minigame(models.Model):
    title = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    short_desc = models.CharField(max_length=200)
