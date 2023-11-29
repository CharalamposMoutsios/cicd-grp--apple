import pytest
from unittest.mock import patch
from datetime import datetime, timedelta, timezone
from pingurl.models import WatchedUrl, PingData
# Your code her
from pingurl.persistance import (
    WatchedUrlNotFoundError,
    add_watched_url,
    get_watched_url,
    delete_watched_url,
    get_url_data,
    get_url_ids,
    add_ping_data,
    get_stats,
)

def test_add_watched_url():
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None)
    url_id = add_watched_url(watched_url)
    assert url_id is not None
    assert url_id in get_url_ids()

def test_get_watched_url():
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None)
    url_id = add_watched_url(watched_url)
    retrieved_url = get_watched_url(url_id)
    assert retrieved_url == watched_url

def test_delete_watched_url():
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None)
    url_id = add_watched_url(watched_url)
    delete_watched_url(url_id)
    with pytest.raises(WatchedUrlNotFoundError):
        get_watched_url(url_id)