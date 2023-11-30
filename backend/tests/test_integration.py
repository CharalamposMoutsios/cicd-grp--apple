# WatchedUrl and Persistance.
from datetime import datetime
import pytest
from pingurl.models import WatchedUrl
from pingurl import persistance

# Skapar ett testobjekt med "övervakningsinformation"
@pytest.fixture
def wu_fixture():
    return WatchedUrl(
        activate_at=datetime(2023, 1, 1),
        force=True,
        period_sec=60,
        url="https://example.com",
    )
# Testar att lägga til och hämta övervakad URL.
def test_integration_wu_and_persistance(wu_fixture):
    # Lägger till övervakad URL och få ID tillbaka.
    url_id = persistance.add_watched_url(wu_fixture)

    # Hämtar övervakad URL med det tilldelade IDt.
    retrieved_watched_url = persistance.get_watched_url(url_id)
    
    #Kollar här om den hämtade URLen är samma som testobjektet.
    assert retrieved_watched_url == wu_fixture
