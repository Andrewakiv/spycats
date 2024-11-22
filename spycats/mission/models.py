from django.db import models
from django.core.validators import MaxLengthValidator


class Mission(models.Model):
    is_completed = models.BooleanField(default=False)


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(
        validators=[MaxLengthValidator(2000)], blank=True, null=True
    )
    is_completed = models.BooleanField(default=False)
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name='targets',
    )
