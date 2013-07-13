from django.db import models

# Create your models here.
class Acronym(models.Model):
    name = models.CharField(max_length=30)
    definition = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    link = models.URLField(blank=True)
