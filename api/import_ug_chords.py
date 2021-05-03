import csv
from django.core.management import BaseCommand
from .models import UGChords

class Command(BaseCommand):
    help = 'Load a chords csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                question = UGChords.objects.create(
                    artist=row[0]
                    song=row[1]
                    ug_chords=row[2]
                )
