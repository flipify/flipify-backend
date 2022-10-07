from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    REQUIRED_FIELDS = ["email"]
