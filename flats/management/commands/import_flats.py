import json
import os

from django.core.management.base import BaseCommand
from flats.models import Flat


class Command(BaseCommand):

    help = "Import flat data from JSON into SQLite database"

    def handle(self, *args, **kwargs):

        file_path = os.path.join(
            "JSON",
            "flats.json"
        )

        with open(file_path, "r") as file:
            data = json.load(file)

        # Remove old data
        Flat.objects.all().delete()

        # Add JSON data into database
        for item in data:

            Flat.objects.create(
                name=item["name"],
                price=item["price"],
                category=item["category"],
                area=item["area"],
                furnished=item["furnished"]
            )

        self.stdout.write(
            self.style.SUCCESS(
                "JSON data successfully imported into SQLite database!"
            )
        )