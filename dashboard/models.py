from django.db import models
from django.contrib.auth.models import User

MOVIMENTATION = (
    ('Entrada', 'Entrada'),
    ('Saída', 'Saída')
)

BRANCH = (
    ('Matriz (01)', 'Matriz (01)'),
    ('Parobé (04)', 'Parobé (04)'),
    ('Campo Bom (11)', 'Campo Bom (11)'),
    ('Dois Irmãos (03 - 05)', 'Dois Irmãos (03 - 05)'),
    ('São Paulo (02)', 'São Paulo (02)'),
)

# Operadores
class Operator(models.Model):
    username = models.CharField(max_length=100, null=True)
    badge = models.IntegerField(null=True, unique=True)
    email = models.EmailField(max_length=254, null=True)
    ranking = models.CharField(max_length=100, null=True, unique=True)
    password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = "Operator"
        verbose_name_plural = "Operators"

# Categories
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# Equipamentos
class Equipment(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

# Sectors
class Sector(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.name}'

# Ordens
class Order(models.Model):
    num_called = models.IntegerField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    information = models.CharField(max_length=255, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50, choices=BRANCH)
    date = models.DateTimeField(auto_now_add=True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True)
    patrimony = models.CharField(max_length=6, blank=True, null=True)
    maq = models.IntegerField(null=True, blank=True)
    movimentation = models.CharField(max_length=10, blank=False, choices=MOVIMENTATION)

    def __str__(self):
        return f'{self.equipment} solicitado por {self.staff.username}'


class Loan(models.Model):
    quantity = models.IntegerField()
    equipment = models.ForeignKey(Equipment, models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    patrimony = models.CharField(max_length=6, blank=True, null=True)
    maq = models.IntegerField(null=True, blank=True)
    retreat_date = models.DateField('Data de Retirada')
    devolution_date = models.DateField('Data de Devolução')

    def __str__(self):
        return f'Loan of {self.quantity} equipment(s) to {self.staff.username}'