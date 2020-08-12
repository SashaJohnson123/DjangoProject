from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    # This is where I would put my own fields to customise it (profile picture etc)
    profile_img = models.URLField(null=True)
    bio_text = models.TextField(null=True)

    def __str__(self):
        return self.username
