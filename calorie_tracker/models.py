from django.db import models
from django.utils import timezone

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.calories} kcal"