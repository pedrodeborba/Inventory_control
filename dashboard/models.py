from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Periféricos', 'Periféricos'),
    ('Notebook', 'Notebook'),
    ('Cabos', 'Cabos')
)

MOVIMENTATION = (
    ('Entrada', 'Entrada'),
    ('Saída', 'Saída')
)

SECTOR = (
    ('TI', 'TI'),
    ('Marketing', 'Marketing'),
    ('Almox', 'Almox')
)

# Operadores
class Operator(models.Model):
    username = models.CharField(max_length=100, null=True)
    badge = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    ranking = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = "Operator"
        verbose_name_plural = "Operators"

#Equipamentos
class Equipment(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=50, blank=False, choices=CATEGORY)

    def __str__(self):
        return f'{self.name}'

#Ordens
class Order(models.Model):
    num_called = models.IntegerField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    sector = models.CharField(max_length=50, choices=SECTOR)
    date = models.DateTimeField(auto_now_add=True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True)
    patrimony = models.CharField(max_length=6, blank=True, null=True)
    maq = models.IntegerField(null=True, blank=True,)
    movimentation = models.CharField(max_length=10, blank=False, choices=MOVIMENTATION)

    def __str__(self):
        return f'{self.equipment} solicitado por {self.staff.username}'

