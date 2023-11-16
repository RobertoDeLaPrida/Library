from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author =  models.CharField(max_length=50)
    rating = models.PositiveBigIntegerField(validators=[MaxValueValidator(5)])
    sinopsis=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title