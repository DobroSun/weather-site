from django.db import models

class City(models.Model):
    name = models.CharField(max_length=126)
    country = models.CharField(max_length=100)

