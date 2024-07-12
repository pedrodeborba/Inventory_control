from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoanForm

# Create your views here.

def dashboard(request):
    return render(request, 'main/dashboard/index.html')

def admins(request):
    admin = 5
    context = {'admin': range(admin)}
    return render(request, 'main/admins/index.html', context)

def operators(request):
    operator = 5
    context = {'operator': range(operator)}
    return render(request, 'main/operators/index.html', context)

def equipments(request):
    equipment = 5
    context = {'equipment': range(equipment)}
    return render(request, 'main/equipments/index.html', context)

def orders(request):
    order = 5
    context = {'order': range(order)}
    return render(request, 'main/orders/index.html', context)

def categories(request):
    category = 5
    context = {'category': range(category)}
    return render(request, 'main/categories/index.html', context)

def loans(request):
    loan = 5
    context = {'loan': range(loan)}
    return render(request, 'main/loans/index.html', context)

def create_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Crie uma instância do objeto Loan a partir do formulário, mas não salve ainda
            loan = form.save(commit=False)
            
            # Limpe todos os equipamentos associados ao objeto loan
            loan.equipment.clear()
            
            # Obtenha os equipamentos selecionados no formulário e adicione ao objeto loan
            selected_equipment = form.cleaned_data['equipment']
            for equipment in selected_equipment:
                loan.equipment.add(equipment)
            
            # Agora sim, salve o objeto loan no banco de dados
            loan.save()
            
            return redirect('dashboard:loans')
    else:
        form = LoanForm()
    
    return render(request, 'main/loans/create_loan.html', {'form': form})