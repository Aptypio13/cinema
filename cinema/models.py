from django.db import models
from cinema.model.film import Film


class FilmEntity(models.Model):
    name = models.CharField(max_length=200, null=False)
    rating = models.IntegerField(default=0)
    description = models.CharField(max_length=700, null=True)
    objects = models.Manager()

    def to_film(self):
        return Film(self.id, self.name, self.rating, self.description)

    def __str__(self):
        return f"name: {self.name}, rating: {self.rating}, description:{self.description}"
