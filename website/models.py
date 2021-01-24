from django.db import models


class Gamemode(models.Model):
    title = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    photo_alt = models.CharField(max_length=100)
    url = models.CharField(max_length=50)
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
