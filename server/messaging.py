from .app import app
from firebase_admin import messaging


def send_data_to_device(data, device):
    app.logger.info(f'sending to device: {device}')

    sanitized = {}
    for k, v in data:
        sanitized[k] = str(v)

    message = messaging.Message(
        data=sanitized,
        token=device,
    )

    production = app.config['FLASK_ENV'] == 'production'
    if production:
        message_id = messaging.send(message)
        app.logger.info(f'successfully sent message to device: {device}')

