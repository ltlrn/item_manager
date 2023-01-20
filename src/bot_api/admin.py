from django.contrib import admin

from bot_api.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "answer")
