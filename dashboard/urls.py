from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('admin/', admin.site.urls),
    path('operators/', views.operators, name='operators'),
    path('equipments/', views.equipments, name='equipments'),
    path('operators/', views.operators, name='operators'),
    path('orders/', views.orders, name='orders'),
    path('categories/', views.categories, name='categories'),
    path('loans/', views.loans, name='loans'),
]