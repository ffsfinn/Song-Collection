from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length = 50)
    artist = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    year = models.IntegerField()

    def __str__(self):
        return self.name