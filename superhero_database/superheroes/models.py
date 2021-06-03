from django.db import models


# Create your models here.
class SuperHeroes(models.Model):
    name = models.CharField(max_length=75)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=75)
    secondary_ability = models.CharField(max_length=75)
    catchphrase = models.CharField(max_length=100)

    def __str__(self):
        return self.name
