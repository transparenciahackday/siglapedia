from django.contrib import admin
from acronyms.models import Acronym

class AcronymAdmin(admin.ModelAdmin):
    list_display = ('name', 'definition', 'description', 'link')

admin.site.register(Acronym, AcronymAdmin)
