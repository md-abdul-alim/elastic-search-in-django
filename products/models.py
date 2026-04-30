from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    sku = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=1000)
   

    def __str__(self) -> str:
        return self.title