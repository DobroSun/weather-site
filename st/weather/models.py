from django.db import models

class City(models.Model):
    city = models.CharField(max_length=126)

