from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CreateUserForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            return redirect('dashboard-index')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)