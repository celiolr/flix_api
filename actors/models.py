from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
)


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True,
                                validators=[MaxValueValidator(limit_value=timezone.now().date(),
                                                              message="Data de Nascimento deve ser menor ou igual a "
                                                                      "data de hoje."),
                                            ],
                                )
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
