from django.db import models
from django.utils.text import slugify

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
    

def chapter_image_upload_path(instance,filename):
    safe_title = slugify(instance.chapter.title)
    return f"chapters/{safe_title}/{filename}"


class ChapterImage(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True,auto_created=True)
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=chapter_image_upload_path)


    