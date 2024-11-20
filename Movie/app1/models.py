from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    language = models.CharField(max_length=30)
    year = models.IntegerField()
    image = models.ImageField(upload_to="image")