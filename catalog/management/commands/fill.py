from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Phones', 'description': 'All phones brand'},
            {'name': 'notebooks', 'description': 'portable PC'},
            {'name': 'PCs', 'description': 'Personal Computer'},
            {'name': 'TVs', 'description': 'telecommunication technology for broadcasting and receiving video '
                                          'and audio over a distance'},
            {'name': 'Headphones', 'description': 'it needs to listen misic quite'}
        ]

        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(
                Category(**category)
            )

        Category.objects.all().delete()

        Category.objects.bulk_create(categories_for_create)
