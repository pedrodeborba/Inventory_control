from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EquipmentForm, LoanForm, StaffForm
from .models import Equipment, Staff
from django.conf import settings

# Create your views here.
@login_required
def index(request):
    return redirect('user-login')

#========================Dashboard==============================

@login_required
def dashboard(request):
    return render(request, 'main/dashboard/index.html')

#========================Operators==============================

@login_required
def operators(request):
    return render(request, 'main/operators/index.html')

#========================Staffs==============================

@login_required
def staffs(request):
    staff = Staff.objects.all()

    context={
        'staff': staff,
    }
    return render(request, 'main/staffs/index.html', context)

@login_required
def create_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-staffs')
    else:
        form = StaffForm()
    
    return render(request, 'main/staffs/create_staff.html', {'form': form})

@login_required
def delete_staff(request, id):
    staff = Staff.objects.get(id=id)
    if request.method == 'POST':
        staff.delete()
        return redirect('dashboard-staffs')
    context = {
        'staff': staff
    }
    return render(request, 'main/staffs/delete_staff.html', context)

@login_required
def update_staff(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('dashboard-staffs')
    else:
        form = StaffForm(instance=staff)
    context = {
        'form': form,
        'staff': staff
    }
    return render(request, 'main/staffs/update_staff.html', context)

#========================Equipments==============================
@login_required
def equipments(request):
    equipment = Equipment.objects.all()

    context={
        'equipment': equipment,
    }
    return render(request, 'main/equipments/index.html', context)

@login_required
def create_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-equipments')
    else:
        form = EquipmentForm()
    
    return render(request, 'main/equipments/create_equipment.html', {'form': form})

@login_required
def delete_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('dashboard-equipments')
    context = {
        'equipment': equipment
    }
    return render(request, 'main/equipments/delete_equipment.html', context)

@login_required
def update_equipment(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('dashboard-equipments')
    else:
        form = EquipmentForm(instance=equipment)
    context = {
        'form': form,
        'equipment': equipment
    }
    return render(request, 'main/equipments/update_equipment.html', context)

#========================Orders==============================
@login_required
def orders(request):
    order = 5
    context = {'order': range(order)}
    return render(request, 'main/orders/index.html', context)

#========================Categories==============================
@login_required
def categories(request):
    category = 5
    context = {'category': range(category)}
    return render(request, 'main/categories/index.html', context)

#========================Loans==============================
@login_required
def loans(request):
    loan = 5
    context = {'loan': range(loan)}
    return render(request, 'main/loans/index.html', context)

@login_required
def create_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)      
            loan.equipment.clear()
            
            selected_equipment = form.cleaned_data['equipment']
            for equipment in selected_equipment:
                loan.equipment.add(equipment)
            
            loan.save()
            
            return redirect('dashboard:loans')
    else:
        form = LoanForm()
    
    return render(request, 'main/loans/create_loan.html', {'form': form})