from datetime import datetime

from pingurl.models import WatchedUrl
from pingurl.persistance import (add_watched_url, delete_watched_url,
                                 get_watched_url)


def test_watched_url_and_persistence():
    activate_at = datetime.now()
    force = True
    period_sec = 60
    url = "http://google.com"

    # Create WatchedUrl and add to persistence
    watched_url = WatchedUrl(activate_at, force, period_sec, url)
    url_id = add_watched_url(watched_url)

    # Retrieve the added WatchedUrl
    retrieved_watched_url = get_watched_url(url_id)
    
    # Test deleting the watched URL
    delete_watched_url(url_id)

    # Assertions
    assert retrieved_watched_url.url == url
    assert retrieved_watched_url.period_sec == period_sec
    assert retrieved_watched_url.force == force
    assert retrieved_watched_url.activate_at == activate_at