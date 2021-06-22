from django.db import models
import string
import random

from django.db.models.enums import Choices

# Create your models here.

class Human(models.Model):
    FLOOR_CHOICES = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    ]
    name = models.CharField(max_length=50, default="Guest")
    company = models.CharField(max_length=100, unique=True, default="none")
    #floor = models.IntegerChoices(choices=FLOOR_CHOICES, default=False)
    created_at = models.DateTimeField(auto_now_add=True)