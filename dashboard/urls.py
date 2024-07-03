from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name='index'),
   path('admins/', views.admins, name='admins'),
   path('equipamentos/', views.equipamentos, name='equipments'),
   path('operadores/', views.operadores, name='operators'),
   path('ordens/', views.ordens, name='orders'),
   path('categorias/', views.categorias, name='categories'),
   path('emprestimos/', views.emprestimos, name='loans'),
]