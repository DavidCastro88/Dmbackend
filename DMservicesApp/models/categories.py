from django.db import models

class Category(models.Model):
    id_category= models.AutoField(primary_key=True, null=False)
    name_category= models.CharField(max_length=255, null=False, blank=False)