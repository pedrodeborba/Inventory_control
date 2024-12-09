# user/views.py

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm, CustomUserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

#=============================Register================================
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard-index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

#=============================Profile=================================
@login_required
def profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'user/profile_update.html', context)

#============================Operators================================
@login_required
def operators(request):
    query = request.GET.get('q', '')
    user_list = User.objects.filter(username__icontains=query)
    context = {
        'user_list': user_list,
        'query': query
    }

    return render(request, 'main/operators/index.html', context)

@login_required
def create_operator(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-operators')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/operators/create_operator.html', {'form': form})

@login_required
def delete_operator(request, id):
    operator = User.objects.get(id=id)
    if request.method == 'POST':
        operator.delete()
        return redirect ('dashboard-operators')
    
    return render(request, 'main/operators/delete_operator.html', {'operator': operator})

@login_required
def update_operator(request, id):
    operator = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=operator)
        if form.is_valid():
            form.save()
            return redirect('dashboard-operators')
    else:
        form = CustomUserUpdateForm(instance=operator)
    context = {
        'form': form,
        'operator': operator
    }
    return render(request, 'main/operators/update_operator.html', context)