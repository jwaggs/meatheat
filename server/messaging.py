from .app import app
from firebase_admin import messaging
import json


def send_data_to_device(data, device):
    app.logger.info(f'sending to device: {device}')

    message_data = {
        'payload': json.dumps(data)
    }
    message = messaging.Message(
        data=message_data,
        token=device,
    )

    try:
        message_id = messaging.send(message)
        app.logger.info(f'successfully sent message {message_id} to device: {device}')
    except Exception as e:
        # TODO: should remove device token from redis if the exception is related to it being invalid.
        app.logger.error(f'error sending message to device: {device} with error: {e}')