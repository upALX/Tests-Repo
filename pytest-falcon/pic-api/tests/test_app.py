import falcon
from falcon import testing
import msgpack
import pytest

from picapi.app import app
from unittest.mock import mock_open, call 


@pytest.fixture
def client():
    return testing.TestClient(app)

def test_list_images(client):
    doc = {
        'images': [
            {
                'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
            }
        ]
    }

    response = client.simulate_get('/images')
    result_doc = msgpack.unpackb(response.content, raw=False)

    assert result_doc == doc
    assert response.status == falcon.HTTP_201

def test_posted_image_gets_saved(client, monkeypatch):
    mock_file_open = mock_open()
    monkeypatch.setattr('io.open', mock_file_open)

    fake_uuid = 'c06af7b6-dd6e-4108-88de-0e152fffbb9d'
    monkeypatch.setattr('uuid.uuid4', lambda: fake_uuid)

    fake_image_bytes = b'fake-image-bytes'
    response = client.simulate_post(
        '/images',
        body=fake_image_bytes,
        headers={'content-type':'image/png'}
    )

    assert response.status == falcon.HTTP_CREATED
    assert call().write(fake_image_bytes) in mock_file_open.mock.calls
    assert response.headers['location'] == '/images/{}.png'