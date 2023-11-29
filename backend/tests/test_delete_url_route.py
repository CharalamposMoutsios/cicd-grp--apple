# backend/tests/test_delete_url_route.py
from pingurl import app, persistance
from flask import Flask

def test_delete_url_route():
    # Skapar en Flask-app i testläge
    app.testing = True
    test_app = app.test_client()

    # Lägger till en övervakad URL först
    data = {
        "activateAt": "2023-01-01T12:00:00Z",
        "force": False,
        "periodSec": 60,
        "url": "http://example.com"
    }
    response = test_app.post('/watched-urls', json=data)
    assert response.status_code == 201

    url_id = response.json['urlId']

    # Testar nu delete-rutten
    response = test_app.delete(f'/watched-urls/{url_id}')

    assert response.status_code == 200

    # Säkerställer att URLen raderas
    with app.app_context():
        try:
            persistance.get_url_data(url_id)
        except persistance.WatchedUrlNotFoundError:
            pass  # URLen ska inte finnas kvar längre
        else:
            assert False, "Watched URL finns fortfarande efter borttagning"
