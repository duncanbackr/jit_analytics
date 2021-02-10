import pytest
import Analytics, Filter, Formating, Query, Sort
from main import main
from Tests.test_integration.fixtures import Flask_Request
from Tests.test_integration.raw_data_comments import raw_data_comments
from Tests.test_integration.raw_data_fans import raw_data_f
from Tests.test_integration.raw_data_filter import raw_data_filter


def test_home():
    flask_request = Flask_Request({})
    response = main(flask_request)
    assert response == {'error': 'must include an okta id'}


def test_fans(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'fans'})
    mocker.patch('Query.db.latest_comments',
        return_value=raw_data_comments)
    response = main(flask_request)
    assert response == raw_data_f


def test_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    response = main(flask_request)
    response = Filter.from_list(response, badge='topFan')
    assert response == raw_data_filter

