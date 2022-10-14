from typing import Optional

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: Optional[str] = None) -> models.Model:
        """Creates and saves a User with the given credentials"""
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email: str, password: str) -> models.Model:
        """Creates and saves a staff user with the provided credientials"""
        user = self.create_user(email, password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str) -> models.Model:
        """Creates an saves a superuser with the provided credientials"""
        user = self.create_user(email, password)
        user.staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []  # email and password is required by default.

    def __str__(self) -> str:
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.is_superuser
