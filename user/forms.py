# user/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Sector

class CustomUserCreationForm(UserCreationForm):
    badge = forms.IntegerField(required=False)
    ranking = forms.CharField(max_length=100, required=False)
    sector = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'badge', 'ranking', 'sector']
