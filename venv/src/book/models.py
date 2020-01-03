from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=120) # max_length=required
    author = models.CharField(max_length=120) # max_length=required
    price = models.DecimalField(decimal_places=2, max_digits=100, null=True)


