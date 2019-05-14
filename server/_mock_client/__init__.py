import requests
import time


def run_mock_controller():
    """Simulate (mock) data coming from a controller such as a raspberry pi"""
    url = 'https://meatheat.herokuapp.com/controllers/1/state/'
    for i in range(180, 190):
        data = [
            {
                'probe': 1,
                'temp': i,
            },
            {
                'probe': 2,
                'temp': i + 5,
            }
        ]

        r = requests.post(url, json=data)
        print(r)
        time.sleep(1)
