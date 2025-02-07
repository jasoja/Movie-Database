from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    studio = models.ForeignKey(Studio, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
