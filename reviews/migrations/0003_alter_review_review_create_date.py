# Generated by Django 5.0.4 on 2024-05-10 20:05

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0002_review_review_create_date_alter_review_stars"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="review_create_date",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 5, 10, 20, 5, 48, 413509, tzinfo=datetime.timezone.utc
                ),
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.date(2024, 5, 10),
                        message="Data de Avaliação deve ser maior ou igual a data de hoje.",
                    )
                ],
            ),
        ),
    ]
