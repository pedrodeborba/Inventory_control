from django import forms
from .models import Staff, Equipment, Loan, Item, Order

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            'item', 'model', 'current_user','manufacturer', 'maq', 'patrimony', 'sn_pn', 
            'cost_center', 'express_code', 'immobilized', 'nf', 'nf_date', 
            'information', 'sector', 'supplier'
        ]
        widgets = {
            'nf_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['username', 'email', 'badge', 'sector', 'ranking']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item']

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