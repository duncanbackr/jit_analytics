import os

import pytest

from flaskr import flaskr


@pytest.fixture
def client():
    flaskr.app.config['TESTING'] = True

    return client

