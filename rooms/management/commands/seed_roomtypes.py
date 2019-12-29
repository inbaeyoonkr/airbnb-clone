from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):
    help = "This command creates room types"

    def handle(self, *args, **options):
        roomtypes = ["Entire place", "Shared room", "Hotel room", "Private room"]

        for r in roomtypes:
            RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS("Roomtypes reated!!!"))
