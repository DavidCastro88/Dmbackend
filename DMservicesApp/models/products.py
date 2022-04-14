from django.db import models
from .categories import Category
from .providers import Provider

class Product(models.Model):
    id_product= models.AutoField(primary_key=True, null=False)
    id_category= models.ForeignKey(Category, on_delete=models.CASCADE)
    id_provider= models.ForeignKey(Provider, on_delete=models.CASCADE)
    description= models.TextField(blank=True, null=False)
    price= models.IntegerField(null=False, blank=False)
    