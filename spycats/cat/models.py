from django.db import models
from mission.models import Mission


class Cat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.SmallIntegerField()
    breed = models.CharField(max_length=100)
    salary = models.SmallIntegerField()
    active_mission = models.OneToOneField(
        Mission,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='assigned_cat'
    )
