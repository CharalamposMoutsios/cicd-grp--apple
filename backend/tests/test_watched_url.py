from datetime import datetime
from pingurl.ping import WatchedUrl

def test_watched_url():
    start_time = datetime.now()
    force = False
    interval = 60
    custom_url = "http://custom-example.com"

    # Testar med anpassad URL
    custom_watched_url = WatchedUrl(start_time, force, interval, custom_url, 1)
    assert custom_watched_url.activate_at == start_time
    assert custom_watched_url.force == force
    assert custom_watched_url.period_sec == interval
    assert custom_watched_url.url == custom_url
    assert custom_watched_url.url_id == 1 

    # Kontrollerar WatchedUrl blir rätt när vi omvandlar det till en dictionary, sträng & repräsentation. 
    assert isinstance(custom_watched_url.to_dict(), dict)
    assert isinstance(str(custom_watched_url), str)
    assert repr(custom_watched_url) == f"WatchedUrl({start_time}, {force}, {interval}, {custom_url}, 1)"
