from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=100, null=True)


