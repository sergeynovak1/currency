from django.urls import path

from .views import CurrencyDetailAPIView, CurrencyListAPIView

urlpatterns = [
    path('currency/<int:pk>', CurrencyDetailAPIView.as_view(), name='currency'),
    path('currencies', CurrencyListAPIView.as_view(), name='currency-list'),
]
