from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from dashboard.models import Operator

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        operator = Operator.objects.filter(username=instance.username).first()
        if operator:
            Profile.objects.create(
                user=instance,
                badge=operator.badge,
                ranking=operator.ranking,
                sector=operator.sector
            )
    else:
        profile = Profile.objects.filter(user=instance).first()
        if profile:
            operator = Operator.objects.filter(username=instance.username).first()
            if operator:
                profile.badge = operator.badge
                profile.ranking = operator.ranking
                profile.sector = operator.sector
                profile.save()
