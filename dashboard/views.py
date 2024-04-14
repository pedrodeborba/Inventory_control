from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/index.html')

def admins(request):
    return render(request, 'links/admins.html')

def operadores(request):
    return render(request, 'links/operadores.html')

def equipamentos(request):
    return render(request, 'links/equipamentos.html')

def ordens(request):
    return render(request, 'links/ordens.html')

def categorias(request):
    return render(request, 'links/categorias.html')

def emprestimos(request):
    return render(request, 'links/emprestimos.html')