from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    """Database model for members"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    profile_pic = models.URLField()
    is_staff = models.BooleanField(default=False)
