from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from movies.models import Movie


# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.'),
        ]
    )
    review_create_date = models.DateTimeField(null=False, blank=False, auto_now_add=True,
                                              validators=[MinValueValidator(limit_value=timezone.now().date(),
                                                                            message="Data de Avaliação deve ser maior "
                                                                                    "ou igual a data de hoje."), ],
                                              )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.__str__()
