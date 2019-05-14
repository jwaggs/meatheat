from .app import app
from firebase_admin import messaging
from server.cache.throttle import set_push_throttle, should_throttle_push
import json


def send(data: dict, device: str, controller: str, push_temp: float = None):
    app.logger.info(f'sending data {"with push" if push_temp else "without push"} to device: {device}')

    message = messaging.Message(
        data={'payload': json.dumps(data)},
        token=device,
    )
    if push_temp and not should_throttle_push(device, controller):
        # don't send another push to this device about this controller for num seconds.
        set_push_throttle(device, controller, seconds=30)
        # add APNS
        message.notification = messaging.Notification(
            title='MeatHeat',
            body=f'{push_temp}° is outside of the range!',
        )
        message.apns = messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=1, sound='default'),
            ),
        )

    try:
        message_id = messaging.send(message)
        app.logger.info(f'successfully sent {message_id} to device: {device}')
    except Exception as e:
        # TODO: should remove device token from redis if the exception is related to it being invalid.
        app.logger.error(f'error sending push to device: {device} with error: {e}')


# def send_data_to_device(data, device):
#     app.logger.info(f'sending data to device: {device}')
#
#     message_data = {
#         'payload': json.dumps(data)
#     }
#     message = messaging.Message(
#         data=message_data,
#         token=device,
#     )
#
#     try:
#         message_id = messaging.send(message)
#         app.logger.info(f'successfully sent message {message_id} to device: {device}')
#         return True
#     except Exception as e:
#         # TODO: should remove device token from redis if the exception is related to it being invalid.
#         app.logger.error(f'error sending message to device: {device} with error: {e}')
#
#     return False
#
#
# def send_push_to_device(device: str, temp, low, high: int):
#     app.logger.info(f'sending push to device: {device}')
#
#     message = messaging.Message(
#         notification=messaging.Notification(
#             title='MEATHEAT',
#             body=f'{temp} is outside of the {low} - {high} range!',
#         ),
#         apns=messaging.APNSConfig(
#             payload=messaging.APNSPayload(
#                 aps=messaging.Aps(badge=1, sound='default'),
#             ),
#         ),
#         token=device,
#     )
#     message.notification = messaging.Notification(
#             title='MEATHEAT',
#             body=f'{temp} is outside of the range!',
#         )
#     message.apns = messaging.APNSConfig(
#             payload=messaging.APNSPayload(
#                 aps=messaging.Aps(badge=1, sound='default'),
#             ),
#         )
#
#     try:
#         message_id = messaging.send(message)
#         app.logger.info(f'successfully sent push {message_id} to device: {device}')
#         return True
#     except Exception as e:
#         # TODO: should remove device token from redis if the exception is related to it being invalid.
#         app.logger.error(f'error sending push to device: {device} with error: {e}')
#
#     return False
