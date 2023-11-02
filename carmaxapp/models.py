from django.db import models

# creating my app templates
class Carmodels(models.Model):
    car = models.CharField(max_length=200)
    description = models.TextField()
    year = models.CharField(max_length=200)
    price = models.CharField(max_length=200)