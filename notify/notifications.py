
from notifications.models import Notification

def get_unread_notifications_user(user):
    unread_notifications = Notification.objects.unread().filter(recipient=user)
    #print(unread_notifications)
    return unread_notifications