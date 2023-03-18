from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from drfguitars.utils.models import AuditedModel


class UserManager(BaseUserManager):

    def create_user(
        self,
        email: str,
        password: str = None,
        is_admin: bool = False
    ):
        u = User(email=email, is_staff=is_admin, is_superuser=is_admin)
        u.set_password(password)
        u.save()

    def create_superuser(self, email: str, password: str = None):
        self.create_user(email, password, is_admin=True)


class User(AbstractUser, AuditedModel):

    email = models.EmailField(
        unique=True,
        error_messages={'unique': 'Email already taken.'}
    )
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
