from django.db import models
from django.contrib.auth.models import AbstractUser
from dashboard.models import Sector

class User(AbstractUser):
    badge = models.IntegerField(null=True, blank=True)
    ranking = models.CharField(max_length=100, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'