from django.contrib import admin
from diseases.models import Disease


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
