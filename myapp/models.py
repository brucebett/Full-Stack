from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        
        user.setpassword(password)
        user.save(using=self._db)
        return user
       