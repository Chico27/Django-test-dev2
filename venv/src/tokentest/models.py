from django.db import models

# Create your models here.
class ProviderToken(models.Model):
    expand_description = models.TextField(blank=True, null=True)
    


