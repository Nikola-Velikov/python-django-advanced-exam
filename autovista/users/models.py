from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

from .managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "This email address is already in use. Please provide a different email.",
            'invalid': "Please provide a valid email address.",
            'blank': "Email address cannot be blank.",
        }
    )

    username = models.CharField(
        max_length=100,
        unique=True,
        error_messages={
            'unique': "This username is already taken. Please choose another one.",
            'blank': "Username cannot be blank.",
            'max_length': "Username cannot exceed 100 characters.",
        }
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    age = models.IntegerField(
        error_messages={
            'invalid': "Age must be a valid integer.",
            'blank': "Age cannot be blank.",
        }
    )

    first_name = models.CharField(
        max_length=30,
        error_messages={
            'blank': "First name cannot be blank.",
            'max_length': "First name cannot exceed 30 characters.",
        }
    )

    last_name = models.CharField(
        max_length=30,
        error_messages={
            'blank': "Last name cannot be blank.",
            'max_length': "Last name cannot exceed 30 characters.",
        }
    )