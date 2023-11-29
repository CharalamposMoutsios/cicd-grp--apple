import pytest
from datetime import datetime, timedelta
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
    #Skapar en WatchedUrl instans för att testa lägga till en Watched URL
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None)
    #Addar en Watched URL och hämtar url_id
    url_id = add_watched_url(watched_url)
    # Checkar att url_id inte är None och att den finns i listan av URL:er
    assert url_id is not None
    assert url_id in get_url_ids()

def test_get_watched_url():
    #Skapar en WatchedUrl instans för att testa hämtning av Watched URL
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None)
     #Addar en Watched URL och hämtar url_id
    url_id = add_watched_url(watched_url)
    # Hämtar Watched URL och checkar att den är samma som den ursprungliga
    retrieved_url = get_watched_url(url_id)
    assert retrieved_url == watched_url

def test_delete_watched_url():
    # Skapar en WatchedUrl instans för att testa borttagning av Watched URL
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        url="http://example.com",
        period_sec=60,
        url_id=None)
    #Addar en Watched URL och hämtar url_id
    url_id = add_watched_url(watched_url)
    # Tar bort Watched URL och checkar så att den inte längre finns
    delete_watched_url(url_id)
    with pytest.raises(WatchedUrlNotFoundError):
        get_watched_url(url_id)

def test_get_url_ids():
    #Skapar två WatchedUrl instanser för att testa hämtning av url_IDs
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
        #Addar två stycken Watched URL:s och hämtar deras url_IDs
    url_id1 = add_watched_url(watched_url1)
    url_id2 = add_watched_url(watched_url2)
    #Hämtar alla URL:er och checkar att antal och url_IDs stämmer
    url_ids = get_url_ids()
    assert len(url_ids) == 4
    assert url_id1 in url_ids
    assert url_id2 in url_ids


def test_get_stats():
    #Skapar två WatchedUrl instanser
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
    # Addar de övervakade URL:erna
    add_watched_url(watched_url1)
    add_watched_url(watched_url2)
    # Skapar två PingData instanser och lägger till dem
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
    # Hämtar statistik och kontrollerar värdena
    stats = get_stats()
    assert stats["watchedUrls"] == 6
    assert stats["pings"] == 2
