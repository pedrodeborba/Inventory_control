from django.db import models
from django.contrib.auth.models import AbstractUser
from dashboard.models import Sector

class User(AbstractUser):
    badge = models.IntegerField('Crachá',null=True, blank=True, unique=True)
    ranking = models.CharField('Cargo', max_length=100, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Setor")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    image = models.ImageField('Imagem de Perfil', default='avatar.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'