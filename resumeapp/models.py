from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Resume(models.Model):
    STATUS_CHOICES = [
        (0, 'не ищет работу'),
        (1, 'в активном поиске'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES)
    grade = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    education = models.CharField(max_length=250)
    experience = models.TextField()
    portfolio = models.CharField(max_length=250)
    title = models.CharField(max_length=150)
    phone = PhoneNumberField(region="RU")
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')

    def __str__(self):
        return self.email
