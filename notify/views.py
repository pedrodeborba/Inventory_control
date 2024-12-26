from django.shortcuts import render, redirect, get_object_or_404
from .notifications import get_unread_notifications_user
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

@login_required
def list_notifications(request):
    unread_notifications = get_unread_notifications_user(request.user)
    return render(request, 'main/notifications/list_notifications.html', {'notifications': unread_notifications})

def unread_notifications_count(request):
    if request.user.is_authenticated:
        unread_count = get_unread_notifications_user(request.user).count()
        return JsonResponse({'unread_count': unread_count})
    return JsonResponse({'unread_count': 0})

def delete_notification(request, notification_id):
    # Obtém a notificação
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    
    # Exclui a notificação
    notification.delete()
    
    # Redireciona de volta para a página de notificações
    return redirect('list_notifications')