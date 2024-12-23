from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
import os
from django.utils import timezone
from notifications.signals import notify
from .models import Card, Loan
from django.contrib.auth import get_user_model
from babel.dates import format_date

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
            
@receiver(post_save, sender=Loan)
def check_loan_due(sender, instance, created, **kwargs):
    current_date = timezone.now().date()
    # Verifica se a data de devolução é anterior à data atual e se não está concluído
    if instance.devolution_date < current_date and not instance.is_completed:
        User = get_user_model()  # Obtém o modelo de usuário personalizado
        users = User.objects.all()  # Obtém todos os usuários
        
        # Dicionário de meses em português
        months = {
            1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
            5: "maio", 6: "junho", 7: "julho", 8: "agosto",
            9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
        }

        # Formatar a data de devolução
        if instance.devolution_date:
            day = instance.devolution_date.day
            month = months[instance.devolution_date.month]
            year = instance.devolution_date.year
            formatted_devolution_date = f"{day} de {month} de {year}"
        else:
            formatted_devolution_date = 'Data inválida'

        # Envia uma notificação para cada usuário
        for user in users:
            notify.send(
                user,
                recipient=user,
                verb=f'O empréstimo passou da data prevista!',
                action_object=instance,
                target=instance.item,
                description=f'O empréstimo de {instance.item} solicitado por {user} venceu dia {formatted_devolution_date}.'
            )

