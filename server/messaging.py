from .app import app


def send_to_device(device):
    app.logger.info(f'sending to device: {device}')
