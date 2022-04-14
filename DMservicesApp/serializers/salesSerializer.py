from DMservicesApp.models.sales import Sale
from rest_framework import serializers

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id_bill', 'id_product','amount']
