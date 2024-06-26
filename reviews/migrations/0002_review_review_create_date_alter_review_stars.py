# Generated by Django 5.0.4 on 2024-05-10 19:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="review_create_date",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 5, 10, 19, 53, 18, 597264, tzinfo=datetime.timezone.utc
                ),
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(
                        limit_value=datetime.date(2024, 5, 10),
                        message="Data de Avaliação deve ser maior ou igual a data de hoje.",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        0, "Avaliação não pode ser inferior a 0 estrelas."
                    ),
                    django.core.validators.MaxValueValidator(
                        5, "Avaliação não pode ser superior a 5 estrelas."
                    ),
                ]
            ),
        ),
    ]
