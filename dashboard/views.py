from django.shortcuts import render
from django.http import HttpResponse

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