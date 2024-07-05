from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Operator, Equipment, Order

admin.site.site_header = 'TI - Usaflex'

class OperatorAdm(admin.ModelAdmin):
    list_display = ('username', 'email', 'badge', 'ranking')
    list_filter = ['ranking']

class EquipmentAdm(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ['category']

class OrderAdm(admin.ModelAdmin):
    list_display = ('num_called', 'equipment', 'staff', 'sector', 'date', 'operator', 'patrimony', 'maq', 'movimentation')
    list_filter = ['equipment', 'staff', 'date', 'sector', 'operator', 'movimentation'] 

# Register your models here
admin.site.unregister(Group)
admin.site.register(Operator, OperatorAdm)
admin.site.register(Equipment, EquipmentAdm)
admin.site.register(Order, OrderAdm)