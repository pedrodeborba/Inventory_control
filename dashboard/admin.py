from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Staff, Equipment, Order, Category, Sector, Loan

admin.site.site_header = 'TI - Usaflex'

class StaffAdm(admin.ModelAdmin):
    list_display = ('username', 'email', 'badge', 'sector', 'ranking')
    list_filter = ['sector', 'ranking']

class EquipmentAdm(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ['category']

class OrderAdm(admin.ModelAdmin):
    list_display = ('num_called', 'equipment', 'staff', 'sector', 'branch', 'date', 'operator', 'patrimony', 'maq', 'movimentation')
    list_filter = ['equipment', 'staff', 'date', 'sector', 'operator', 'movimentation'] 

class LoanAdm(admin.ModelAdmin):
    list_display = ('quantity', 'equipment', 'staff', 'patrimony', 'maq', 'retreat_date', 'devolution_date')

# Register your models here
admin.site.unregister(Group)
admin.site.register(Staff, StaffAdm)
admin.site.register(Equipment, EquipmentAdm)
admin.site.register(Order, OrderAdm)
admin.site.register(Category)
admin.site.register(Sector)
admin.site.register(Loan, LoanAdm)
