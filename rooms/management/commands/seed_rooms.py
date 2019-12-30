import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Seed(Seed):
    @classmethod
    def faker(cls, locale=None, codename=None):
        code = codename or cls.codename(locale)
        if code not in cls.fakers:
            from faker import Faker

            cls.fakers[code] = Faker(locale)
            cls.fakers[code].seed_instance(random.randint(1, 10000))
        return cls.fakers[code]


class Command(BaseCommand):
    help = "This command created rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=100,
            type=int,
            help="How many rooms do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
                "guests": lambda x: random.randint(1, 20),
            },
        )
        create_photos = seeder.execute()
        create_clean = flatten(list(create_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in create_clean:
            room_instance = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(3, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"room_photos/{random.randint(1,31)}.webp",
                    room=room_instance,
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_instance.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_instance.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_instance.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!!!"))
