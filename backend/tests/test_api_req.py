import os
import requests


API_URL = f"http://{os.environ['CONTAINER_IP']}:5000"


def test_set_watched_url():
    to_post = {
        "activateAt": "2023-11-06T01:36:28.610Z",
        "force": True,
        "periodSec": 30,
        "url": "https://klockren.nu",
    }
    assert requests.post(f"{API_URL}/watched-urls", json=to_post, timeout=20).json() == {
        "message": "Watched URL added",
        "urlId": 2,
    }

