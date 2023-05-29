from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from userapp.models import User
from .models import Resume


class ResumeTestCase(APITestCase):
    endpoint = '/api/v1/resume/'

    def setUp(self):
        self.user, created = User.objects.get_or_create(username='test', password='test')
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.resume = Resume.objects.create(
            status=1,
            grade='grade',
            specialty='specialty',
            salary=1000.00,
            education='education',
            experience='experience',
            portfolio='portfolio',
            title='title',
            phone='+79111111111',
            email='email@example.com',
            user=self.user
        )

    def test_get_resume(self):
        response = self.client.get(f'{self.endpoint}{self.resume.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 1)
        self.assertEqual(response.data['grade'], 'grade')
        self.assertEqual(response.data['specialty'], 'specialty')
        self.assertEqual(response.data['salary'], '1000.00')
        self.assertEqual(response.data['education'], 'education')
        self.assertEqual(response.data['experience'], 'experience')
        self.assertEqual(response.data['portfolio'], 'portfolio')
        self.assertEqual(response.data['title'], 'title')
        self.assertEqual(response.data['phone'], '+79111111111')
        self.assertEqual(response.data['email'], 'email@example.com')

    def test_patch_resume(self):
        data = {
            'status': 0,
            'grade': 'new grade',
            'specialty': 'new specialty',
            'salary': 2000.00,
            'education': 'new education',
            'experience': 'new experience',
            'portfolio': 'new portfolio',
            'title': 'new title',
            'phone': '+79111111112',
            'email': 'new_email@example.com'
        }
        response = self.client.patch(f'{self.endpoint}{self.resume.id}/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 0)
        self.assertEqual(response.data['grade'], 'new grade')
        self.assertEqual(response.data['specialty'], 'new specialty')
        self.assertEqual(response.data['salary'], '2000.00')
        self.assertEqual(response.data['education'], 'new education')
        self.assertEqual(response.data['experience'], 'new experience')
        self.assertEqual(response.data['portfolio'], 'new portfolio')
        self.assertEqual(response.data['title'], 'new title')
        self.assertEqual(response.data['phone'], '+79111111112')
        self.assertEqual(response.data['email'], 'new_email@example.com')
