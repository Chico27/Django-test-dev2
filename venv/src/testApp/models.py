from django.db import models

# Create your models here.
class testModel1(models.Model):
    testField = ArrayField(models.IntegerField(null=False, blank=False), null=True, blank=True)