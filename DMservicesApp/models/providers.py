from django.db import models

class Provider(models.Model):
    id_provider = models.AutoField(primary_key=True, null=False)
    names = models.CharField('Name', max_length = 40)
    lastnames = models.CharField('LastNames', max_length = 40,null=True)
    business = models.CharField('Business', max_length = 40, null=True)
    cellphone = models.CharField('Cellphone', max_length =20)
    address = models.CharField('Address', max_length=40)