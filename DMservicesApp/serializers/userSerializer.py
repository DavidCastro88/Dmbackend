from rest_framework import serializers
from DMservicesApp.models.user import User
from DMservicesApp.models.account import Account
from DMservicesApp.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name','lastnames', 'email', 'cellphone','address' 'account']
    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'lastnames': user.lastnames,
            'email': user.email,
            'cellphone': user.cellphone,
            'address': user.address,
            'account': {
                'id': account.id,
                'lastChangeDate': account.lastChangeDate,
                'isActive': account.isActive
                }
            }


