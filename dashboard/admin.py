from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Admin

admin.site.site_header = 'TI - Usaflex'

class AdminAdm(admin.ModelAdmin):
    list_display = ('usuario', 'email', 'cracha', 'cargo')
    list_filter = ['cargo']

#Register your models here
admin.site.unregister(Group)
admin.site.register(Admin, AdminAdm)

