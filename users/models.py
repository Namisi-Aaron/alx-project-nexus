from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom User model that extends AbstractUser.

    Additional attributes:
        role: User role (admin or user).
        phone_number: Unique phone number for each user.
    """
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
        """
        Save method to set the role to 'admin' for superusers
        and 'user' for non-superusers.
        """
        if self.is_superuser:
            self.role = 'admin'
        elif not self.role:
            self.role = 'user'
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the CustomUser model.
        """
        return f"{self.username} - {self.role}"
