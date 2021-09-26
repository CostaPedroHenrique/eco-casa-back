from rest_framework import viewsets

from .serializers import BalanceSerializer, DepositSerializer, MaterialSerializer

from apps.deposit.models import Balance, Deposit, Material


class BalanceViewSet(viewsets.ModelViewSet):
  queryset = Balance.objects.all()
  serializer_class = BalanceSerializer

class DepositViewSet(viewsets.ModelViewSet):
  queryset = Deposit.objects.all()
  serializer_class = DepositSerializer

class MaterialViewSet(viewsets.ModelViewSet):
  queryset = Material.objects.all()
  serializer_class = MaterialSerializer
