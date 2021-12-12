from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
  PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user.

        Args:
            email (str): email for the new user
            password (str, optional): password for new user. Defaults to None.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a new superuser.

        Args:
            email (str): email for the new user
            password (str, optional): password for new user. Defaults to None.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True  # permissions mixin
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
