from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EquipmentForm, StaffForm, ItemForm, OrderForm, LoanForm
from .models import Equipment, Staff, Item, Order, Loan
from django.conf import settings
#=============================Index=================================
@login_required
def index(request):
    return redirect('user-login')

#========================Dashboard==============================

@login_required
def dashboard(request):
    return render(request, 'main/dashboard/index.html')

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

#========================Items==============================
@login_required
def items(request):
    item = Item.objects.all()

    context={
        'item': item,
    }
    return render(request, 'main/items/index.html', context)

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-items')
    else:
        form = ItemForm()
    return render(request, 'main/items/create_item.html', {'form': form})

@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-items')
    context = {
        'item': item
    }
    return render(request, 'main/items/delete_item.html', context)

@login_required
def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-items')
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'main/items/update_item.html', context)

#========================Orders==============================
@login_required
def orders(request):
    order = Order.objects.all()
    context = {'order': order}
    return render(request, 'main/orders/index.html', context)

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-orders')
    else:
        form = OrderForm()
    return render(request, 'main/orders/create_order.html', {'form': form})

@login_required
def delete_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard-orders')
    context = {
        'order': order
    }
    return render(request, 'main/orders/delete_order.html', context)

@login_required
def update_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard-orders')
    else:
        form = OrderForm(instance=order)
    context = {
        'form': form,
        'order': order
    }
    return render(request, 'main/orders/update_order.html', context)

def process_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    equipment = order.equipment
    
    if order.movimentation == Order.EXIT:
        # Se for uma saída, atualiza o equipamento com o funcionário atual
        equipment.current_user = order.staff
    elif order.movimentation == Order.ENTRY:
        # Se for uma entrada, o responsável volta a ser o 'Estoque da TI'
        equipment.current_user = None  # ou se tiver um usuário específico para o estoque, defina aqui

    equipment.save()

#========================Loans==============================
@login_required
def loans(request):
    loan = Loan.objects.all()
    context = {'loan': loan}
    return render(request, 'main/loans/index.html', context)

@login_required
def create_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-loans')
    else:
        form = LoanForm()
    return render(request, 'main/loans/create_loan.html', {'form': form})

@login_required
def delete_loan(request, id):
    loan = Loan.objects.get(id=id)
    if request.method == 'POST':
        loan.delete()
        return redirect('dashboard-loans')
    context = {
        'loan': loan
    }
    return render(request, 'main/loans/delete_loan.html', context)

@login_required
def update_loan(request, id):
    loan= get_object_or_404(Loan, id=id)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('dashboard-loans')
    else:
        form = LoanForm(instance=loan)
    context = {
        'form': form,
        'loan': loan
    }
    return render(request, 'main/loans/update_loan.html', context)