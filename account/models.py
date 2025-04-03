from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True, unique=True, error_messages={'unique': 'A user with that phone number already exists.'})
    profile_image = models.ImageField(upload_to='images/user_profile', blank=True, null=True)


    def __str__(self):
        return self.username