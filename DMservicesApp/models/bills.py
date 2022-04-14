from django.db import models
from .user import User
from datetime import datetime,date

class Bill(models.Model):
    id_bill = models.AutoField(primary_key=True, null=False)
    id_user=models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    