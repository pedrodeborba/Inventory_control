from django.db import models

class Admin(models.Model):
    usuario = models.CharField(max_length=100, null=True)
    cracha = models.IntegerField(null=True)
    senha = models.CharField(max_length=128, null=True)
    email = models.EmailField(max_length=254, null=True)
    cargo = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name="Admin"
        verbose_name_plural="Admins"

