from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('badge', 'sector', 'ranking')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'badge', 'sector', 'ranking')

class CustomUserAdm(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'badge', 'sector', 'ranking', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'sector')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'badge', 'sector', 'ranking')
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'badge', 'sector', 'ranking')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'badge', 'sector', 'ranking'),
        }),
    )

class ProfileAdm(admin.ModelAdmin):
    list_display = ('user', 'image')

admin.site.register(Profile, ProfileAdm)
admin.site.register(User, CustomUserAdm)
