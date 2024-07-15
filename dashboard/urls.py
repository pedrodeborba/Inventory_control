from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('dashboard', views.index, name='dashboard-index'),
    path('admin/', admin.site.urls),
    path('admins', views.admins, name='admins'),
    path('operators/', views.operators, name='operators'),
    path('equipments/', views.equipments, name='equipments'),
    path('operators/', views.operators, name='operators'),
    path('orders/', views.orders, name='orders'),
    path('categories/', views.categories, name='categories'),
    path('loans/', views.loans, name='loans'),
    path('loans/create/', views.create_loan, name='create_loan'),
]