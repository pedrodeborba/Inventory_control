from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard-index'),
    path('admins/', views.admins, name='dashboard-admins'),
    path('operators/', views.operators, name='dashboard-operators'),
    path('equipments/', views.equipments, name='dashboard-equipments'),
    path('equipments/create/', views.create_equipment, name='dashboard-create-equipment'),
    path('equipments/delete/<int:id>/', views.delete_equipment, name='dashboard-delete-equipment'),
    path('equipments/update/<int:id>/', views.update_equipment, name='dashboard-update-equipment'),
    path('operators/', views.operators, name='dashboard-operators'),
    path('orders/', views.orders, name='dashboard-orders'),
    path('categories/', views.categories, name='dashboard-categories'),
    path('loans/', views.loans, name='dashboard-loans'),
    path('loans/create/', views.create_loan, name='dashboard-create-loan'),
]