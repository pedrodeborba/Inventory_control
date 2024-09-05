from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_delete, post_save, pre_save
import os
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(staff=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
# Função auxiliar para deletar um arquivo de imagem
def delete_image(image_path):
    if image_path and os.path.isfile(image_path):
        os.remove(image_path)

# Sinal para deletar a imagem antiga ao substituir por uma nova no modelo Profile
@receiver(pre_save, sender=Profile)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # Novo perfil, sem necessidade de deletar nada
    try:
        old_image = Profile.objects.get(pk=instance.pk).image
    except Profile.DoesNotExist:
        return  # Perfil não existe, nada para deletar

    # Se a imagem antiga é diferente da nova imagem, delete a antiga
    new_image = instance.image
    if old_image and old_image != new_image and old_image.name != 'avatar.png':
        delete_image(old_image.path)

# Sinal para deletar a imagem do perfil quando o objeto Profile for deletado
@receiver(post_delete, sender=Profile)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image and instance.image.name != 'avatar.png':
        delete_image(instance.image.path)

# Sinal para deletar a imagem do perfil quando o usuário for deletado
@receiver(post_delete, sender=User)
def delete_user_profile_image(sender, instance, **kwargs):
    try:
        profile = instance.profile
        if profile.image and profile.image.name != 'avatar.png':
            delete_image(profile.image.path)
    except Profile.DoesNotExist:
        pass  # Se o perfil não existe, nada para deletar