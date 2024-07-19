from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard-index'),
    path('admin/', admin.site.urls),
    path('admins', views.admins, name='dashboard-admins'),
    path('operators/', views.operators, name='dashboard-operators'),
    path('equipments/', views.equipments, name='dashboard-equipments'),
    path('operators/', views.operators, name='dashboard-operators'),
    path('orders/', views.orders, name='dashboard-orders'),
    path('categories/', views.categories, name='dashboard-categories'),
    path('loans/', views.loans, name='dashboard-loans'),
    path('loans/create/', views.create_loan, name='dashboard-create_loan'),
]