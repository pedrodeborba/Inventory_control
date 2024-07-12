from django import forms
from .models import Loan
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class LoanForm(forms.ModelForm):
    retreat_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=DateInput(format='%d/%m/%Y'))
    devolution_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=DateInput(format='%d/%m/%Y'))

    class Meta:
        model = Loan
        fields = ['quantity', 'equipment', 'staff', 'patrimony', 'maq', 'retreat_date', 'devolution_date']
