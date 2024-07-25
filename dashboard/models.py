from django.db import models
from django.conf import settings
import pytz
from django.utils import timezone

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

# Sectors
class Sector(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.name}'

# Operadores
class Staff(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    badge = models.IntegerField(null=True, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True)
    ranking = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.username}'

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

# Ordens
class Order(models.Model):
    num_called = models.IntegerField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50, choices=BRANCH)
    date = models.DateTimeField(auto_now_add=True)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    patrimony = models.CharField(max_length=6, blank=True, null=True, unique=True)
    maq = models.IntegerField(null=True, blank=True)
    movimentation = models.CharField(max_length=10, blank=False, choices=MOVIMENTATION)

    def __str__(self):
        return f'{self.equipment} solicitado por {self.staff.username}'
    
    def formatted_date(self):
        # Define o fuso horário de Brasília
        brasilia_tz = pytz.timezone('America/Sao_Paulo')
        # Converte a data armazenada no banco de dados para o fuso horário de Brasília
        local_date = self.date.astimezone(brasilia_tz)
        # Formata a data para dd/mm/yyyy às HH:MM
        return local_date.strftime('%d/%m/%Y às %H:%M')


class Loan(models.Model):
    quantity = models.IntegerField()
    equipment = models.ForeignKey(Equipment, models.CASCADE, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    patrimony = models.CharField(max_length=6, blank=True, null=True, unique=True)
    maq = models.IntegerField(null=True, blank=True)
    retreat_date = models.DateField('Data de Retirada')
    devolution_date = models.DateField('Data de Devolução')

    def formatted_retreat_date(self):
        return self.retreat_date.strftime('%d/%m/%Y')
    
    def formatted_devolution_date(self):
        return self.devolution_date.strftime('%d/%m/%Y')

    def __str__(self):
        return f'Empréstimo de {self.equipment} solicitado por {self.staff.username}'