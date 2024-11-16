from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, username, email, password, **other_fields):
        if not email:
            raise ValueError("Email field must be set")
        
        email = self.normalize_email(email)
        other_fields.setdefault('is_active', True)
        user = self.model(username, email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,  email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser+True.')
        
        return self.create_user(username, email, password, **other_fields)
        
        


class CustomUser(AbstractUser, PermissionsMixin):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    objects = CustomAccountManager()

    def __str__(self):
        return self.username



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

