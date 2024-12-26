function updateNotificationCount() {
    fetch('/notifications/unread_count/')
        .then(response => response.json())
        .then(data => {
            const badge = document.querySelector('.nav-item .badge');
            if (data.unread_count > 0) {
                if (badge) {
                    badge.textContent = data.unread_count;
                } else {
                    const span = document.createElement('span');
                    span.className = 'badge bg-primary rounded-circle';
                    span.textContent = data.unread_count;
                    document.querySelector('#notificationDropdown').appendChild(span);
                }
            } else if (badge) {
                badge.remove();
            }
        })
        .catch(error => console.error('Erro ao buscar notificações:', error));
}

// Atualiza as notificações a cada minuto
setInterval(updateNotificationCount, 60000);

// Atualiza ao carregar a página
updateNotificationCount();
