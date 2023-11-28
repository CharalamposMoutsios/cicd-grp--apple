import pytest
from datetime import datetime
from pingurl.models import WatchedUrl


def test_watched_url_creation():
    activate_at = datetime.now()
    force = True
    period_sec = 60
    valid_url = "http://example.com"

    # Test valid instantiation
    watched_url = WatchedUrl(activate_at, force, period_sec, valid_url)
    assert watched_url.activate_at == activate_at
    assert watched_url.force == force
    assert watched_url.period_sec == period_sec
    assert watched_url.url == valid_url

    # Test invalid URL
    with pytest.raises(ValueError):
        WatchedUrl(activate_at, force, period_sec, "invalid_url")