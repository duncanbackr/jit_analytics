import pytest
from main import main
from Tests.test_integration.fixtures import Flask_Request
from Tests.test_integration.raw_data import raw_data


def test_home():
    flask_request = Flask_Request({})
    response = main(flask_request)
    assert response == {'error': 'must include an okta id'}


def test_fans(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'fans'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data)
    response = main(flask_request)
    assert response == {}
