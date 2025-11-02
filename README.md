# Notification Service API

API для отправки уведомлений через Email, SMS, Telegram.

## Запуск

```bash
make dev-up
# или
docker compose -f docker-compose.dev.yml up -d

# Применить миграции
docker exec notification-service-api alembic upgrade head
```

Сервис: `http://localhost:8000`
Документация: `http://localhost:8000/docs`

## API

### POST /api/v1/users
Создание пользователя

```json
{
  "email": "user@example.com",
  "phone": "+79991234567",
  "telegram_id": "123456789"
}
```

### POST /api/v1/notifications/send
Отправка уведомления

```json
{
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "body": "Текст уведомления"
}
```

**Ответ:**
```json
{
  "id": "...",
  "channel_used": "email",
  "status": "sent"
}
```

Каналы доставки по приоритету: Email → SMS → Telegram
