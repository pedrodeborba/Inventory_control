from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name='index'),
   path('admins/', views.admins, name='admins'),
   path('equipamentos/', views.equipamentos, name='equipamentos'),
   path('operadores/', views.operadores, name='operadores'),
   path('ordens/', views.ordens, name='ordens'),
   path('categorias/', views.categorias, name='categorias'),
   path('emprestimos/', views.emprestimos, name='emprestimos'),
]