from DMservicesApp.models.products import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id_category', 'id_provider','description','price']
