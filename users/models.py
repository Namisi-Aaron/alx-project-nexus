from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    USER_ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default='user',
    )
    phone_number = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'admin'
        elif not self.role:
            self.role = 'user'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.role}"
