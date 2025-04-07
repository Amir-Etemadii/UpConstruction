from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/user_profile', blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'.title()

    def __str__(self):
        return self.username