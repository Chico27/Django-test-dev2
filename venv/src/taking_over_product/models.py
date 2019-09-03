from django.db import models
from products.models import Product

# Create your models here.
class TakingOverProduct(Product):
    taking_over_description = models.TextField(blank=True, null=True)

