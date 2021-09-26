from rest_framework import serializers 

from apps.deposit.models import Balance, Deposit, Material

class BalanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Balance
    fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
  class Meta:
    model = Deposit
    fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
  class Meta:
    model = Material
    fields = '__all__'
