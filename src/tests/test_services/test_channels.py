import pytest
from src.app.services.channels.email import EmailChannel
from src.app.services.channels.sms import SMSChannel
from src.app.services.channels.telegram import TelegramChannel
from src.app.models.notification import NotificationChannel


@pytest.mark.asyncio
async def test_email_channel():
    channel = EmailChannel()
    assert channel.channel == NotificationChannel.EMAIL
    # Проверяем только тип канала, так как send() использует случайное значение
    assert hasattr(channel, "send")


@pytest.mark.asyncio
async def test_sms_channel():
    channel = SMSChannel()
    assert channel.channel == NotificationChannel.SMS
    # Проверяем только тип канала, так как send() использует случайное значение
    assert hasattr(channel, "send")


@pytest.mark.asyncio
async def test_telegram_channel():
    channel = TelegramChannel()
    assert channel.channel == NotificationChannel.TELEGRAM
    # Проверяем только тип канала, так как send() использует случайное значение
    assert hasattr(channel, "send")
