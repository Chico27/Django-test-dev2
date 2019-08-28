from django.db import models
from products.models import Product

# Create your models here.
class ExpandProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    expand_description = models.TextField(blank=True, null=True)


