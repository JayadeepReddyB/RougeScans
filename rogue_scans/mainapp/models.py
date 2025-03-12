from django.db import models

# Create your models here.

class Manga(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(default = None)
    pic = models.ImageField(upload_to = "mangas/", null = True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    chapter_number = models.PositiveBigIntegerField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.manga.name} - Chapter {self.chapter_number}: {self.title}"
    


