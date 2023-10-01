from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@online-shop.com',
            first_name='Admin',
            last_name='online-shop',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123qwe456rty')
        user.save()
