from django.db import models
from django.forms import ModelForm

# Create your models here.
class Acronym(models.Model):
    name = models.CharField(max_length=30)
    definition = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    link = models.URLField(blank=True)

class AcronymForm(ModelForm):
    class Meta:
        model = Acronym
        #fields = ['__all__']
        #localized_fields = ['__all__']

