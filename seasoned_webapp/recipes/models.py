from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    kcal = models.IntegerField(default=-1)
    energy = models.IntegerField(default=-1)
    sugar = models.IntegerField(default=-1)
    salt = models.IntegerField(default=-1)
    carbohydrates = models.IntegerField(default=-1)
    protein = models.IntegerField(default=-1)

    def __str__(self):
        return self.name


class Appliances(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Wishes(models.Model):
    wish = models.CharField(max_length=300)

    def __str__(self):
        return self.wish
    

class Nationalities(models.Model):
    nationality = models.CharField(max_length=300)

    def __str__(self):
        return self.nationality


class SeasonsHolidays(models.Model):
    name = models.CharField(max_length=300)

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
    appliances = models.ManyToManyField(Appliances, blank=True)
    wishes = models.ManyToManyField(Wishes, blank=True)
    nationality = models.ManyToManyField(Nationalities, blank=True)
    seasonsHolidays = models.ManyToManyField(SeasonsHolidays, blank=True)


    def __str__(self):
        return self.title



    




