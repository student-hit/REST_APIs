from django.db import models

# Create your models here.

class Product(models.Model):
     name = models.CharField(max_length=120)
     price = models.FloatField()
     category = models.CharField(max_length=35)
     description = models.TextField()

     def __str__(self):
          return f"{self.name} | {self.category} ({str(self.price)}) Rs."
     
