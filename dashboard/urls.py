from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard-index'),
    path('operators/', views.operators, name='dashboard-operators'),
    #========================Staffs==============================
    path('staffs/', views.staffs, name='dashboard-staffs'),
    path('staffs/create/', views.create_staff, name='dashboard-create-staff'),
    path('staffs/delete/<int:id>/', views.delete_staff, name='dashboard-delete-staff'),
    path('staffs/update/<int:id>/', views.update_staff, name='dashboard-update-staff'),
    #========================Equipments==============================
    path('equipments/', views.equipments, name='dashboard-equipments'),
    path('equipments/create/', views.create_equipment, name='dashboard-create-equipment'),
    path('equipments/delete/<int:id>/', views.delete_equipment, name='dashboard-delete-equipment'),
    path('equipments/update/<int:id>/', views.update_equipment, name='dashboard-update-equipment'),
    
    path('orders/', views.orders, name='dashboard-orders'),
    path('categories/', views.categories, name='dashboard-categories'),
    path('loans/', views.loans, name='dashboard-loans'),
    path('loans/create/', views.create_loan, name='dashboard-create-loan'),
]