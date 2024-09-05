from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from .models import Card

# Função auxiliar para remover a imagem do sistema de arquivos
def remove_image(image_path):
    if image_path and os.path.isfile(image_path):
        try:
            os.remove(image_path)
            print(f"Imagem removida: {image_path}")
        except Exception as e:
            print(f"Erro ao deletar a imagem: {e}")
    else:
        print(f"O arquivo não existe: {image_path}")

# Sinal para deletar a imagem quando o objeto do modelo Card for deletado
@receiver(post_delete, sender=Card)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        print(f"Tentando deletar a imagem: {instance.image.path}")
        remove_image(instance.image.path)

# Sinal para deletar a imagem antiga ao substituir por uma nova no modelo Card
@receiver(pre_save, sender=Card)
def delete_image_on_change(sender, instance, **kwargs):
    # Verifique se o objeto já existe no banco de dados (edição de um objeto existente)
    if instance.pk:
        try:
            old_instance = Card.objects.get(pk=instance.pk)
        except Card.DoesNotExist:
            return

        # Comparar se a imagem foi modificada
        if old_instance.image and old_instance.image != instance.image:
            print(f"Tentando deletar a imagem antiga: {old_instance.image.path}")
            remove_image(old_instance.image.path)
