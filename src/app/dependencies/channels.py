from src.app.services.channels.email import EmailChannel
from src.app.services.channels.sms import SMSChannel
from src.app.services.channels.telegram import TelegramChannel
from src.app.services.channels.base import BaseChannel


def get_channels() -> dict[str, BaseChannel]:
    return {
        "email": EmailChannel(),
        "phone": SMSChannel(),
        "telegram_id": TelegramChannel(),
    }
