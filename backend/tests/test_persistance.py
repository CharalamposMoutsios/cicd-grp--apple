import pytest
from unittest.mock import patch
from datetime import datetime, timedelta, timezone
from pingurl.models import WatchedUrl, PingData

from pingurl.persistance import (
    WatchedUrlNotFoundError,
    add_watched_url,
    get_watched_url,
    delete_watched_url,
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

def test_get_url_ids():
    watched_url1 = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None)
    watched_url2 = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.se",
        period_sec=60,
        url_id=None)
    url_id1 = add_watched_url(watched_url1)
    url_id2 = add_watched_url(watched_url2)
    url_ids = get_url_ids()
    assert len(url_ids) == 4
    assert url_id1 in url_ids
    assert url_id2 in url_ids


def test_get_stats():
    watched_url1 = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None,
    )
    watched_url2 = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.se",
        period_sec=60,
        url_id=None,
    )
    add_watched_url(watched_url1)
    add_watched_url(watched_url2)
    ping_data1 = PingData(
        pinged_at=datetime.now(),
        response_time_sec=timedelta(seconds=1),
        url_id=0,
        status_code=200)
    ping_data2 = PingData(
        pinged_at=datetime.now(),
        response_time_sec=timedelta(seconds=1),
        url_id=1,
        status_code=200)
    add_ping_data(ping_data1)
    add_ping_data(ping_data2)
    stats = get_stats()
    assert stats["watchedUrls"] == 6
    assert stats["pings"] == 2
