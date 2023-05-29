from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from resume.env import env

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(
                email=env('DJANGO_SUPERUSER_EMAIL'),
                username=env('DJANGO_SUPERUSER_USERNAME'),
                password=env('DJANGO_SUPERUSER_PASSWORD'),
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
