from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return render(request, 'main/dashboard/index.html')

def admins(request):
    admin = 5
    context = {'admin': range(admin)}
    return render(request, 'main/admins/index.html', context)

def operadores(request):
    operador = 5
    context = {'operador': range(operador)}
    return render(request, 'main/operadores/index.html', context)

def equipamentos(request):
    equipamento = 5
    context = {'equipamento': range(equipamento)}
    return render(request, 'main/equipamentos/index.html', context)

def ordens(request):
    ordem = 5
    context = {'ordem': range(ordem)}
    return render(request, 'main/ordens/index.html', context)

def categorias(request):
    categoria = 5
    context = {'categoria': range(categoria)}
    return render(request, 'main/categorias/index.html', context)

def emprestimos(request):
    emprestimo = 5
    context = {'emprestimo': range(emprestimo)}
    return render(request, 'main/emprestimos/index.html', context)