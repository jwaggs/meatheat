import requests
import time


def run_mock_controller():
    """Test our copy utility statistics endpoint"""
    url = 'https://meatheat.herokuapp.com/controllers/1/state/'
    for i in range(150, 160):
        data = [
            {
                'id': 1,
                'temp': i,
            }
        ]
        r = requests.post(url, json=data)
        print(r)
        time.sleep(1)
