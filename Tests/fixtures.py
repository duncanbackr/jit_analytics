import os

import pytest

# from flaskr import flaskr
import flask

@pytest.fixture
def client():
    flask.app.config['TESTING'] = True

    return flask.app.test_client()

