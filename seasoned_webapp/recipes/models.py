from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    kcal = models.IntegerField()
    energy = models.IntegerField()
    sugar = models.IntegerField()
    salt = models.IntegerField()
    carbohydrates = models.BigIntegerField()
    protein = models.IntegerField()

    def __str__(self):
        return self.name


class Appliance(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField('recipe title', max_length=120)
    description = models.TextField()
    author = models.CharField(max_length=120)
    date = models.DateTimeField()
    nationality = models.CharField(max_length=120)
    season = models.CharField(max_length=120)
    difficulty = models.IntegerField()
    ingredient = models.ManyToManyField(Ingredient, blank=True)
    appliance = models.ManyToManyField(Appliance, blank=True)


    def __str__(self):
        return self.title
    




