import pytest
from Tests.fixtures import client

def test_no_okta(client):
    """Start with a blank database."""

    response = client.get('/')
    assert response.json() == ""