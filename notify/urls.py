from django.urls import path
from . import views

urlpatterns = [
    path('list_notifications/', views.list_notifications, name='list_notifications'),
    path('unread_count/', views.unread_notifications_count, name='unread_notifications_count'),
    path('delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
]
