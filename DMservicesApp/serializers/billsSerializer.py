from DMservicesApp.models.bills import Bill
from rest_framework import serializers

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id_user', 'date']