from django.contrib.auth.models import User
from django.core.management import BaseCommand
from apps.search.models import Account


class Command(BaseCommand):

    help = "import lib"

    def handle(self, *args, **options):
        # Parce some file
        for i in range(1000, 2000):
            a = Account.objects.create(name = 'test {}'.format(i))
            print(a.id)
       
