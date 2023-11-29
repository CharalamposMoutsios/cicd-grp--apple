# Models and persistance.

from datetime import datetime
import pytest
from pingurl.models import WatchedUrl
from pingurl import persistance


@pytest.fixture
def wu_fixture():
    return WatchedUrl(
        activate_at=datetime(2023, 1, 1),
        force=True,
        period_sec=60,
        url="https://example.com",
    )

def test_integration_wu_and_persistance(wu_fixture):
    url_id = persistance.add_watched_url(wu_fixture)

    retrieved_watched_url = persistance.get_watched_url(url_id)
    assert retrieved_watched_url == wu_fixture
