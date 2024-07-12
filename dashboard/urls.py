from django.urls import path
from . import views
from django.contrib import admin

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls, name='admin'),
    path('admins', views.admins, name='admins'),
    path('operators/', views.operators, name='operators'),
    path('equipments/', views.equipments, name='equipments'),
    path('operators/', views.operators, name='operators'),
    path('orders/', views.orders, name='orders'),
    path('categories/', views.categories, name='categories'),
    path('loans/', views.loans, name='loans'),
    path('loans/create/', views.create_loan, name='create_loan'),
]