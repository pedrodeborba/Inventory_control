from .notifications import get_unread_notifications_user

def unread_notifications_context(request):
    if request.user.is_authenticated:
        unread_notifications = get_unread_notifications_user(request.user)
        unread_count = unread_notifications.count()
        return {
            'unread_notifications_count': unread_count,
            'notifications': unread_notifications,
        }
    return {
        'unread_notifications_count': 0,
        'notifications': [],
    }
