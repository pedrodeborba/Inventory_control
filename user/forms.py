from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Sector, Profile

class CustomUserCreationForm(UserCreationForm):
    badge = forms.IntegerField(required=False)
    ranking = forms.CharField(max_length=100, required=False)
    sector = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'badge', 'ranking', 'sector']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance', None)
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Um usuário com este nome de usuário já existe.")
        return username

class CustomUserUpdateForm(forms.ModelForm):
    badge = forms.IntegerField(required=False)
    ranking = forms.CharField(max_length=100, required=False)
    sector = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False)
    password1 = forms.CharField(required=False, widget=forms.PasswordInput)
    password2 = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'badge', 'ranking', 'sector']

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.instance = kwargs.get('instance', None)
        if self.instance:
            self.fields['password1'].required = False
            self.fields['password2'].required = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Um usuário com este nome de usuário já existe.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        user = super(CustomUserUpdateForm, self).save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'badge', 'ranking', 'sector']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
