from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EquipmentForm, StaffForm, ItemForm, OrderForm, LoanForm
from .models import Equipment, Staff, Item, Order, Loan, Card
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import TruncMonth
#=============================Index=================================
@login_required
def index(request):
    return redirect('user-login')

#========================Dashboard==============================

@login_required
def dashboard(request):
    # Cards
    cards = Card.objects.all()
    
    #Enviando o total de Funcionários
    total_staffs = Staff.objects.count()
    
    # Horário das orderns para o quarto gráfico
    orders = Order.objects.order_by('-views')[:5]
    formatted_orders = [
        {
            'date_formatted': order.date.strftime('%d/%m/%y às %H:%M'),
            'movimentation': order.movimentation,
            'equipment': order.equipment,
        }
        for order in orders
    ]
    
    context = {
        #cards
        'cards': cards,
        
        #staffs
        'total_staffs': total_staffs,
        
        #orders
        'orders': formatted_orders,
    }
    
    return render(request, 'main/dashboard/index.html', context)

#========================Graphics============================

def chart_data(request):
    # ====================================
    # Total de ordens e ordens por filial
    # ====================================
    orders_by_date = Order.objects.values('date__date').annotate(total_orders=Count('id')).order_by('date__date')
    orders_by_branch = Order.objects.values('branch').annotate(total_orders=Count('id')).order_by('branch')
    orders_by_month = Order.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_orders=Count('id')).order_by('month')

    dates = [order['date__date'].strftime('%d/%m') for order in orders_by_date]
    totals = [order['total_orders'] for order in orders_by_date]
    
    data_by_month = {
        'labels': [order['month'].strftime('%B %Y') for order in orders_by_month],
        'data': [order['total_orders'] for order in orders_by_month],
    }

    data_by_branch = {
        'labels': [order['branch'] for order in orders_by_branch],
        'data': [order['total_orders'] for order in orders_by_branch],
    }
    
    order_chart = {
        'dates': dates,
        'totals': totals,
    }
    
    # ===============
    # Dados do Staff
    # ===============
    staff_data = Staff.objects.values('sector__name').annotate(count=Count('id')).order_by('sector__name')
    staff_labels = [data['sector__name'] for data in staff_data]
    staff_counts = [data['count'] for data in staff_data]
    total_staffs = Staff.objects.count()

    staff_chart_data = {
        'labels': staff_labels,
        'data': staff_counts,
        'total_staffs': total_staffs
    }

    # =============================
    # Dados para o gráfico de pizza
    # =============================
    equipment_data = Equipment.objects.values('item__item').annotate(count=Count('id')).order_by('item__item')
    labels = [data['item__item'] for data in equipment_data]
    data = [data['count'] for data in equipment_data]
    
    pie_chart_data = {
        'labels': labels,
        'data': data
    }

    # ==============================
    # Dados para o gráfico de barras
    # ==============================
    orders_data = Order.objects.values('date__week_day').annotate(count=Count('id')).order_by('date__week_day')
    days_of_week = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    bar_labels = days_of_week[:len(orders_data)]
    bar_data = [data['count'] for data in orders_data]

    bar_chart_data = {
        'labels': bar_labels,
        'data': bar_data
    }
    
    # ======================
    # Gráfico de empréstimos
    # ======================
    loans_by_date = Loan.objects.values('retreat_date').annotate(total_loans=Count('id')).order_by('retreat_date')
   
    loans_by_month = Loan.objects.annotate(month=TruncMonth('retreat_date')).values('month').annotate(total_loans=Count('id')).order_by('month')
    
    loan_dates = [loan['retreat_date'].strftime('%d/%m') for loan in loans_by_date if loan['retreat_date'] is not None]
    loan_totals = [loan['total_loans'] for loan in loans_by_date]
    
    loan_data_by_month = {
        'loan_labels': [loan['month'].strftime('%B %Y') for loan in loans_by_month if loan['month'] is not None],
        'loan_data': [loan['total_loans'] for loan in loans_by_month],
    }
    
    loan_chart = {
        'loan_dates': loan_dates,
        'loan_totals': loan_totals,
    }

    # Resposta completa em json
    return JsonResponse({
        #order
        'order_chart': order_chart,
        'orders_by_month': data_by_month,
        'orders_by_branch': data_by_branch,
        
        #staff
        'staff_chart_data': staff_chart_data,
        
        
        'pie_chart_data': pie_chart_data,
        'bar_chart_data': bar_chart_data,
        
        #loan
        'loan_chart': loan_chart,
        'loans_by_month': loan_data_by_month
    })

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