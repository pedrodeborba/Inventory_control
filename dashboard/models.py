from django.db import models
from django.conf import settings
import pytz
from django.utils import timezone

BRANCH = (
    ('Matriz (01)', 'Matriz (01)'),
    ('Parobé (04)', 'Parobé (04)'),
    ('Campo Bom (11)', 'Campo Bom (11)'),
    ('Dois Irmãos (03 - 05)', 'Dois Irmãos (03 - 05)'),
    ('São Paulo (02)', 'São Paulo (02)'),
)

# Setores
class Sector(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.name}'

# Funcionários
class Staff(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    badge = models.IntegerField(null=True, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True)
    ranking = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.username}'

# Itens
class Item(models.Model):
    item = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.item}'

# Equipamentos
class Equipment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    manufacturer = models.CharField('Fabricante', max_length=255, blank=True, null=True)
    model = models.CharField('Modelo', max_length=255, blank=True, null=True)
    current_user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_equipment') #Reponsável pelo equipamento
    maq = models.IntegerField('Maq', null=True, blank=True)
    patrimony = models.IntegerField('Patrimônio', blank=True, null=True, unique=True)
    sn_pn = models.CharField('S/N - P/N', max_length=50, blank=True, null=True)
    cost_center = models.IntegerField('Centro de Custo', blank=True, null=True)
    express_code = models.CharField('Express Code', max_length=255, blank=True, null=True)
    immobilized = models.IntegerField('Imobilizado', blank=True, null=True)
    nf = models.CharField('NF', max_length=50, blank=True, null=True)
    nf_date = models.DateField('Data NF', null=True, blank=True)
    information = models.TextField('Informações', blank=True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True)
    supplier = models.CharField('Fornecedor', max_length=255, blank=True, null=True)

    def __str__(self):
        parts = [
            f"{self.item or '[Nome não especificado]'}",
            f"{self.model or '[Modelo não especificado]'}",
        ]
        
        if self.maq:
            parts.append(f"MAQ: {self.maq}")
        if self.patrimony:
            parts.append(f"Patrimônio: {self.patrimony}")
        if self.sn_pn:
            parts.append(f"SN/PN: {self.sn_pn}")
        
        return ", ".join(parts)

# Ordens
class Order(models.Model):
    ENTRY = 'E'
    EXIT = 'S'
    MOVIMENTATION = (
        (ENTRY, 'Entrada'),
        (EXIT, 'Saída')
    )
    
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
    movimentation = models.CharField(max_length=1, blank=False, choices=MOVIMENTATION)

    def __str__(self):
        return f'{self.equipment} solicitado por {self.staff.username}'
    
    def formatted_date(self):
        # Define o fuso horário de Brasília
        brasilia_tz = pytz.timezone('America/Sao_Paulo')
        # Converte a data armazenada no banco de dados para o fuso horário de Brasília
        local_date = self.date.astimezone(brasilia_tz)
        # Formata a data para dd/mm/yyyy às HH:MM
        return local_date.strftime('%d/%m/%Y às %H:%M')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.movimentation == self.EXIT:
            self.equipment.current_user = self.staff
        elif self.movimentation == self.ENTRY:
            self.equipment.current_user = None
        self.equipment.save()

# Empréstimos
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

# Cards
class Card(models.Model):
    title = models.CharField('Título', max_length=99, blank=True)
    subtitle = models.CharField('Subtítulo', max_length=99, blank=True)
    image = models.ImageField('Imagem', upload_to='cards/images/', blank=True, null=True)
    link = models.CharField('Levar para', max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title or self.subtitle or "Sem título ou subtítulo"