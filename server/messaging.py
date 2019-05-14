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


def send_push_to_device(device: str, temp, low, high: int):
    message = messaging.Message(
        notification=messaging.Notification(
            title='MEATHEAT',
            body=f'{temp} is outside of the {low} - {high} range!',
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=1, sound='default'),
            ),
        ),
        token=device,
    )

    try:
        message_id = messaging.send(message)
        app.logger.info(f'successfully sent push {message_id} to device: {device}')
    except Exception as e:
        # TODO: should remove device token from redis if the exception is related to it being invalid.
        app.logger.error(f'error sending push to device: {device} with error: {e}')
