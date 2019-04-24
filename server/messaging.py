from .app import app
from firebase_admin import messaging


def send_data_to_device(data, device):
    app.logger.info(f'sending to device: {device}')

    sanitized = {}
    for k, v in data.items():
        sanitized[k] = str(v)

    message = messaging.Message(
        data=sanitized,
        token=device,
    )

    try:
        message_id = messaging.send(message)
        app.logger.info(f'successfully sent message {message_id} to device: {device}')
    except Exception as e:
        # TODO: should remove device token from redis if the exception is related to it being invalid.
        app.logger.info(f'error sending message to device: {device} with error: {e}')
