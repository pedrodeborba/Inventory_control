from django.contrib import admin
from .models import Profile

class ProfileAdm(admin.ModelAdmin):
    list_display = ('user', 'image')

admin.site.register(Profile, ProfileAdm)
