from django.db import models

# Create your models here.

class Manga(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(default = None)
    pic = models.ImageField(upload_to = "mangas/", null = True)

    def __str__(self):
        return self.name
