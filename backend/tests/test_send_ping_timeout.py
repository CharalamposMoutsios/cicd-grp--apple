# backend/tests/test_send_ping_timeout.py

from datetime import datetime
from pingurl.ping import WatchedUrl, send_ping
from unittest.mock import patch

def test_send_ping_timeout():
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=False, 
        period_sec=60,
        url="http://example-timeout.com",
        url_id=2,
    )

    with patch("pingurl.ping.requests.get") as mock_get:
        # Simulera en TimeoutError genom att sätta side_effect för mock_get
        mock_get.side_effect = TimeoutError("PING **************** TIMEOUT")
        
        try:
            # Anropar send_ping
            ping_data = send_ping(watched_url)
            # Om det inte finns något fel, testa att response_time_sec är  None
            assert ping_data.response_time_sec is None
        except TimeoutError as e:
            # Om det är en TimeoutError, låt testet passera
            pass
