from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Disease(models.Model):
    """Disease model, obviously."""

    title = models.CharField(max_length=200)
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class Symptom(models.Model):
    """Single symptom, one of a kind."""
    
    title = models.CharField(max_length=200)
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class DiseaseHistory(models.Model):
    """Disease-symptom-person relations."""

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Больной",
    )

    disease = models.ForeignKey(
        'diseases.Disease',
        on_delete=models.SET_NULL, # обязательны два следующих аргумента
        null = True,
        blank = True,
        verbose_name="Заболевание",
    )

    symptom = models.ManyToManyField(
        'diseases.Symptom', # читай про циркулярный импорт!!!
        verbose_name="Симптом",
    )

    first_symtoms = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Начало болезни",
    )

    recovered = models.DateTimeField(
        null = True,
        blank = True,
        verbose_name="Окончание болезни",
    )
