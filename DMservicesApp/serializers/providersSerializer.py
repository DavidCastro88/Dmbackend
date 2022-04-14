from DMservicesApp.models.providers import Provider
from rest_framework import serializers

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['names', 'lastnames','business','cellphone','address']

