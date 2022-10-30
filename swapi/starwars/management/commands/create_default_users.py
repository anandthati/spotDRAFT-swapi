from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = """
    This command creates the Employee roles.
    """

    def handle(self, *args, **options):
        print("Creating default users")
        user_data = [
            {
                "username": "anand+1@gmail.com",
                "email": "anand+1@gmail.com",
                "first_name": "Anand",
                "last_name": "Thati",
            },
            {
                "username": "anand+2@gmail.com",
                "email": "anand+2@gmail.com",
                "first_name": "John",
                "last_name": "Thati",
            },
            {
                "username": "anand+3@gmail.com",
                "email": "anand+3@gmail.com",
                "first_name": "Edward",
                "last_name": "Thati",
            },
        ]
        for data in user_data:
            user, created = User.objects.get_or_create(**data)
            print(f"{user.email} is created with id {user.id}")
        print("Successfully created default user!")

