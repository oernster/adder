import pytest

import adder


@pytest.fixture
def client():
    adder.app.config['TESTING'] = True
    client = adder.app.test_client()

    with adder.app.app_context():
        # perform init stuff if required
        pass
    yield client


def test_total(client):
    """Test endpoint."""
    data = {
        "total": list(range(10000001)),
    }

    t = client.get('/total')
    assert t.get_json() == data