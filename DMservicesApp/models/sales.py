from django.db import models
from .products import Product
from .bills import Bill

class Sale(models.Model):
    id_sale= models.AutoField(primary_key=True, null=False)
    id_bill= models.ForeignKey(Bill, on_delete=models.CASCADE)
    id_product=models.ForeignKey(Product, on_delete=models.CASCADE)
    amount= models.IntegerField(null=False, blank=False)