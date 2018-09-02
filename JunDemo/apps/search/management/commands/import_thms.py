from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    help = "Import data from ss_struct schema (org. structure, user assignments)"

    def create_parser(self, prog_name, subcommand):
        parser = super().create_parser(prog_name, subcommand)

        parser.add_argument(
            '--clean-eid-null', '-c',
            action='store',
            dest='clean',
            help="Clean records with empty external_id",
            default='no',
            choices=['yes', 'no']
        )
        return parser

    def handle(self, *args, **options):
        clean = options['clean'] == 'yes'

       
