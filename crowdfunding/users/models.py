from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class CustomUser(AbstractUser):
    password = models.CharField(max_length=80, verbose_name="password")
    first_name = models.CharField(max_length=50, verbose_name="first name")
    last_name = models.CharField(max_length=50, verbose_name="last name")
    image = models.URLField(max_length=200, verbose_name="profile photo", default="https://via.placeholder.com/300.jpg")
    bio = models.TextField(max_length=1000, verbose_name="biography", default='SOME STRING')
    phone = models.CharField(max_length=13, verbose_name="phone number", default = '0481041798')
    location = models.CharField(max_length=100, verbose_name="location", default = 'Brisbane')
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    def user(self):
        return self.id
    def __str__(self):
        return self.username

#the lines bellow cause the token creation when a user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)