from django.urls import path
from . import views
from user import views as user_views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard-index'),
    path('dashboard/chart-data/', views.chart_data, name='chart-data'),
     #========================================================Users=======================================
    path('operators/', user_views.operators, name='dashboard-operators'),
    path('operators/create/', user_views.create_operator, name='dashboard-create-operator'),
    path('operators/delete/<int:id>/', user_views.delete_operator, name='dashboard-delete-operator'),
    path('operators/update/<int:id>/', user_views.update_operator, name='dashboard-update-operator'),
    #========================Staffs==============================
    path('staffs/', views.staffs, name='dashboard-staffs'),
    path('staff/<int:staff_id>/', views.detail_staff, name='dashboard-detail-staff'),
    path('staffs/create/', views.create_staff, name='dashboard-create-staff'),
    path('staffs/delete/<int:id>/', views.delete_staff, name='dashboard-delete-staff'),
    path('staffs/update/<int:id>/', views.update_staff, name='dashboard-update-staff'),
    #========================Equipments==============================
    path('equipments/', views.equipments, name='dashboard-equipments'),
    path('equipments/create/', views.create_equipment, name='dashboard-create-equipment'),
    path('equipments/delete/<int:id>/', views.delete_equipment, name='dashboard-delete-equipment'),
    path('equipments/update/<int:id>/', views.update_equipment, name='dashboard-update-equipment'),
    #========================items==============================
    path('items/', views.items, name='dashboard-items'),
    path('items/create/', views.create_item, name='dashboard-create-item'),
    path('items/delete/<int:id>/', views.delete_item, name='dashboard-delete-item'),
    path('items/update/<int:id>/', views.update_item, name='dashboard-update-item'),
    #========================Orders==============================
    path('orders/', views.orders, name='dashboard-orders'),
    path('orders/<int:order_id>/', views.detail_order, name='dashboard-detail-order'),
    path('orders/create/', views.create_order, name='dashboard-create-order'),
    path('orders/delete/<int:id>/', views.delete_order, name='dashboard-delete-order'),
    path('orders/update/<int:id>/', views.update_order, name='dashboard-update-order'),
    path('orders/process/<int:order_id>', views.process_order, name='dashboard-process-order'),
    #========================Loans==============================
    path('loans/', views.loans, name='dashboard-loans'),
    path('loans/create/', views.create_loan, name='dashboard-create-loan'),
    path('loans/delete/<int:id>/', views.delete_loan, name='dashboard-delete-loan'),
    path('loans/update/<int:id>/', views.update_loan, name='dashboard-update-loan'),
    path('loans/<int:pk>/', views.detail_loan, name='dashboard-detail-loan'),
]