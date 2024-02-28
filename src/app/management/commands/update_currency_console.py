from django.core.management.base import BaseCommand

from app.models import Currency


class Command(BaseCommand):
    help = 'Creating and changing a currency object using the console'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Currency name')
        parser.add_argument('rate', type=float, help='Currency rate')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        rate = kwargs['rate']

        currency = Currency.objects.filter(name=name).first()
        if currency:
            currency.rate = rate
            currency.save(update_fields=['rate'])
            self.stdout.write(self.style.SUCCESS(f'Successfully updated currency: {name} with rate: {rate}'))
        else:
            Currency.objects.create(name=name, rate=rate)
            self.stdout.write(self.style.SUCCESS(f'Successfully created currency: {name} with rate: {rate}'))
