from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    pin_code = models.CharField(max_length=6)

    def __str__(self):
        return self.type

