from django.db import models

CATEGORY = (
    ('Periféricos', 'Periféricos'),
    ('Notebook', 'Notebook'),
    ('Cabos', 'Cabos')
)

class Equipment(models.Model):
    name = models.CharField(max_lenght=100, blank=False)
    specification = models.CharField(max_lengh=255, blank=False)
    quantity = models.IntegerField(blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY)
    patrimony = models.IntegerField(blank=True)
    maq = models.IntegerField(prefix = 'MAQ',blank=True)

class Admin(models.Model):
    username = models.CharField(max_length=100, null=True)
    badge = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    ranking = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=128, null=True)

    class Meta:
        verbose_name="Admin"
        verbose_name_plural="Admins"

