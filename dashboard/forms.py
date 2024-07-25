from django import forms
from .models import Staff, Equipment, Loan, Category, Order

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'category']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['username', 'email', 'badge', 'sector', 'ranking']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['num_called', 'equipment', 'information', 'staff', 'sector', 'branch', 'operator', 'patrimony', 'maq', 'movimentation']
        labels = {
            'num_called': 'Chamado',
            'equipment': 'Equipamento',
            'information': 'Informação',
            'staff': 'Solicitante',
            'sector': 'Setor',
            'branch': 'Filial',
            'operator': 'Operador',
            'patrimony': 'Patrimônio (opcional)',
            'maq': 'Maq (opcional)',
            'movimentation': 'Movimentação',
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['quantity', 'equipment', 'staff', 'patrimony', 'maq', 'retreat_date', 'devolution_date']