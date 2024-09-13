from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Staff, Equipment, Order, Item, Sector, Loan, Card

admin.site.site_header = 'TI - Usaflex'

class StaffAdm(admin.ModelAdmin):
    list_display = ('username', 'email', 'badge', 'sector', 'ranking')
    list_filter = ['sector', 'ranking']

class EquipmentAdm(admin.ModelAdmin):
    list_display = (
        'item', 'model', 'manufacturer', 'maq', 'patrimony', 'sn_pn', 
        'cost_center', 'express_code', 'immobilized', 'nf', 'nf_date', 
        'information', 'sector', 'supplier'
    )
    list_filter = ['manufacturer', 'sector', 'immobilized']
    search_fields = ['item', 'patrimony', 'model', 'sn_pn', 'cost_center', 'express_code', 'nf', 'supplier']
    ordering = ['item']

class OrderAdm(admin.ModelAdmin):
    exclude = ('views',)
    list_display = ('num_called', 'equipment', 'staff', 'sector', 'branch', 'date', 'operator', 'patrimony', 'maq', 'movimentation')
    list_filter = ['equipment', 'staff', 'date', 'sector', 'operator', 'movimentation'] 

class LoanAdm(admin.ModelAdmin):
    exclude = ('views',)
    list_display = ('quantity', 'equipment', 'staff', 'patrimony', 'maq', 'retreat_date', 'devolution_date')
    
class CardAdm(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'link')

# Register your models here
admin.site.unregister(Group)
admin.site.register(Staff, StaffAdm)
admin.site.register(Equipment, EquipmentAdm)
admin.site.register(Order, OrderAdm)
admin.site.register(Item)
admin.site.register(Sector)
admin.site.register(Loan, LoanAdm)
admin.site.register(Card, CardAdm)
