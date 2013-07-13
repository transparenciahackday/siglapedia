# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Acronym(models.Model):
    name = models.CharField("Sigla", help_text="A sigla que queres adicionar", max_length=30)
    definition = models.CharField("Definição", help_text="O significado exato da sigla", max_length=300)
    description = models.TextField("Descrição", help_text="O que é esta entidade? Descreve-a com uma frase. A Wikipédia ajuda!", max_length=5000)
    link = models.URLField("Link", help_text="Link para obter mais informação sobre esta sigla. Nós gostamos de links da Wikipédia em vez de links institucionais, sempre que possível.", blank=True)

class AcronymForm(ModelForm):
    class Meta:
        model = Acronym
        #fields = ['__all__']
        #localized_fields = ['__all__']

