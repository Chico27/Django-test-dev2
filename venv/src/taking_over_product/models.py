from django.db import models
from products.models import Product

# Create your models here.
class TakingOverProduct(Product):
    taking_over_description = models.TextField(blank=True, null=True)
    limit_price = models.DecimalField(decimal_places=2, max_digits=1000)

