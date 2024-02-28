from django.core.management.base import BaseCommand
import requests
from xml.etree import ElementTree

from app.models import Currency


class Command(BaseCommand):
    help = 'Creating and changing a currency object using the parsing'

    def handle(self, *args, **kwargs):
        response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
        tree = ElementTree.fromstring(response.content)

        for valute in tree.findall('Valute'):
            name = valute.find('Name').text
            rate = valute.find('Value').text.replace(',', '.')
            currency = Currency.objects.filter(name=name).first()
            if currency:
                currency.rate = rate
                currency.save(update_fields=['rate'])
            else:
                Currency.objects.create(name=name, rate=rate)

        self.stdout.write(self.style.SUCCESS(f'Сurrencies were successfully updated using the link'))
