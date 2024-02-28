from rest_framework import generics, permissions

from .models import Currency
from .serializers import CurrencySerializer


class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrencyDetailAPIView(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
