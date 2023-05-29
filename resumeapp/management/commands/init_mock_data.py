from django.core.management.base import BaseCommand

from resumeapp.models import Resume
from userapp.models import User

MOCK_USERNAME = 'test'
MOCK_PASSWORD = 'test'


class MockData:
    def add(self):
        self.add_user()
        self.add_resume()

    def add_user(self):
        user, created = User.objects.get_or_create(username=MOCK_USERNAME)
        self.user = user
        user.set_password(MOCK_PASSWORD)
        user.save()
        print("Добавили пользователя:", user)

    def add_resume(self):
        data = {
            'status': 1,
            'grade': 'test grade',
            'specialty': 'test specialty',
            'salary': 2000.00,
            'education': 'test education',
            'experience': 'test experience',
            'portfolio': 'test portfolio',
            'title': 'test title',
            'phone': '+79331111111',
            'email': 'test_email@example.com',
            'user': self.user
        }
        resume, created = Resume.objects.get_or_create(**data)
        print("Добавили резюме:", resume)


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Resume.objects.count() == 0:
            MockData().add()
