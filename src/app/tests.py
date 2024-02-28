from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import Currency


class CurrencyAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = str(RefreshToken.for_user(self.user).access_token)

        Currency.objects.create(name='USD', rate=75.5)
        Currency.objects.create(name='EUR', rate=90.2)

    def test_currency_list_api(self):
        url = '/currencies'
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_currency_detail_api(self):
        currency = Currency.objects.get(name='USD')
        url = f'/currency/{currency.id}'
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'USD')
        self.assertEqual(float(response.data['rate']), 75.5)
