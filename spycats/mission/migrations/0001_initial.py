# Generated by Django 5.1.3 on 2024-11-22 10:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Target",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxLengthValidator(2000)],
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "mission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="targets",
                        to="mission.mission",
                    ),
                ),
            ],
        ),
    ]
