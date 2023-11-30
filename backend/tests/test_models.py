from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta
from pingurl.models import WatchedUrl, PingData
import pytest

# Skapar ett testobjekt av WatchedUrl.
@pytest.fixture
def wu_fixture():
    return WatchedUrl(
        activate_at=datetime(2023, 1, 1),
        force=True,
        period_sec=60,
        url="https://example.com",
        url_id=1,
    )

# Skapar ett testobjekt av PingData.
@pytest.fixture
def ping_data_fixture():
    return PingData(
        pinged_at=datetime(2023, 1, 1, 12, 0, 0),
        response_time_sec=timedelta(seconds=1),
        status_code=200,
        url_id=1,
    )

# Test för att testa skapandet av WatchedUrl objekt.
@patch("pingurl.models.WatchedUrl", MagicMock)
def test_wu_creation(wu_fixture):
    assert wu_fixture.activate_at == datetime(2023, 1, 1)
    assert wu_fixture.force
    assert wu_fixture.period_sec == 60
    assert wu_fixture.url == "https://example.com"
    assert wu_fixture.url_id == 1

# Test för att testa skapandet av PingData-Objekt.
@patch("pingurl.models.PingData", MagicMock)
def test_ping_data_creation(ping_data_fixture):
    assert ping_data_fixture.pinged_at == datetime(2023, 1, 1, 12, 0, 0)
    assert ping_data_fixture.response_time_sec == timedelta(seconds=1)
    assert ping_data_fixture.status_code == 200
    assert ping_data_fixture.url_id == 1

@patch("pingurl.models.validators.url", return_value=False)
def test_invalid_url(mock_validators_url):
    # Testfunktion för att kontrollera om WatchedUrl constructor kastar ett ValueError när URL:en som getts är ogiltig.
    with pytest.raises(ValueError, match="url must be a valid URL string"):
        WatchedUrl(
            activate_at=datetime(2023, 1, 1),
            force=True,
            period_sec=60,
            url="invalid_url", #Detta ska trigga ett ValueError
            url_id=1,
        )
    #Checkar att mocken faktiskt anropades med den angivna URL:en
    mock_validators_url.assert_called_once_with("invalid_url")