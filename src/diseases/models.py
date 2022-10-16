from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Disease(models.Model):
    """Disease model, obviously."""

    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Symptom(models.Model):
    """Single symptom, one of a kind."""

    # SYSTEMS = {
        # "N": "nervous system",
        # "E": "endocrine system",
        # another systems...
    #}

    # system = models.CharField(max_length=1, choices=SYSTEMS)
    description = models.TextField

    # class Meta:
        # ordering = ["system"]

    def __str__(self):
        return self.description[:100]


class DiseaseHistory:
    """Disease-symptom-person relations."""

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="diseases",
        verbose_name="Больной",
    )

    disease = models.ForeignKey(
        Disease,
        on_delete=models.SET_NULL,
        related_name="diseases",
        verbose_name="Заболевание",
    )

    symptom = models.ManyToManyField(
        Symptom,
    )

    first_symtoms = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Начало болезни",
    )

    recovered = models.DateTimeField(
        verbose_name="Окончание болезни",
    )
