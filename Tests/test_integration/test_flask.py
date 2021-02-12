import pytest
import datetime
import Analytics, Filter, Formating, Query, Sort
from main import main
from Tests.test_integration.fixtures import Flask_Request
from Tests.test_integration.raw_data_comments import raw_data_comments, raw_data_comments2
from Tests.test_integration.response_data_fans import mock_fans
from Tests.test_integration.response_data_filter import mock_filter_badge
from Tests.test_integration.response_data_sort import mock_growth, mock_balance, mock_retain, mock_badge
from Tests.test_integration.response_data_class import mock_positive, mock_negative, mock_other, mock_suggest, mock_question

def test_home():
    flask_request = Flask_Request({})
    response = main(flask_request)
    assert response == {'error': 'must include an okta id'}

def test_fans(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'fans'})

    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_fans

def test_topfan_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'badge':'topFan'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_filter_badge

def test_archive_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00uw0rxwf7dgiIs3w4x6', 'resource':'comments', 'archived':True})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == []

def test_video_filter(mocker):
    for videoid, video_title in [('365z', 'My Girl | The Temptations | Matt Mulholland Cover')]:
        flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'videoId':videoid})
        mocker.patch('Query.latest_comments',
            return_value=raw_data_comments)
        mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
        response = main(flask_request)

        for row in response:
            assert row['videoTitle'] == video_title

def test_multiple_video_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'videoId':'365z366z'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    
    video_title_list = ['My Girl | The Temptations | Matt Mulholland Cover', 'And So It Goes by Billy Joel | Matt Mulholland & Chris Bill Cover']

    for row in response:
        assert row['videoTitle'] in video_title_list

def test_all_badges_filter(mocker):
    for badge in ['newFan', 'trendingFan', 'topFan', 'reEngageFan']:
        flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'badge':badge})
        mocker.patch('Query.latest_comments',
            return_value=raw_data_comments)
        mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
        response = main(flask_request)

        for row in response:
            assert row['badge'] == badge

def test_all_badges_fans_filter(mocker):
    for badge in ['newFan', 'trendingFan', 'topFan', 'reEngageFan']:
        flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'fans', 'badge':badge})
        mocker.patch('Query.latest_comments',
            return_value=raw_data_comments)
        mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
        response = main(flask_request)

        for row in response:
            assert row['badge'] == badge

def test_positive_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Positive'})
    mocker.patch('Query.latest_comments',
         return_value=raw_data_comments2)
    response = main(flask_request)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_positive

def test_negative_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Negative', 'perPage':1})
    mocker.patch('Query.latest_comments',
         return_value=raw_data_comments2)
    response = main(flask_request)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_negative

def test_other_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Other', 'perPage':2})
    mocker.patch('Query.latest_comments',
         return_value=raw_data_comments2)
    response = main(flask_request)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_other

def test_suggest_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Suggestion', 'perPage':2})
    mocker.patch('Query.latest_comments',
         return_value=raw_data_comments2)
    response = main(flask_request)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_suggest

def test_question_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Question', 'perPage':2})
    mocker.patch('Query.latest_comments',
         return_value=raw_data_comments2)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_question

def test_sort_timestamp(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'timestamp'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response[1]['commentDatePosted'] > response[2]['commentDatePosted'] 

def test_sort_growth(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'growth','perPage':10})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))    
    response = main(flask_request)
    assert response == mock_growth

def test_sort_balanced(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'order':'balanced', 'perPage':10})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_balance

def test_sort_retain(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'retention', 'perPage':10})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)

    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
    response = main(flask_request)
    assert response == mock_retain

def test_sort_badge(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'badge_score', 'perPage':10})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)

    mocker.patch('Analytics.datetime_now',
        return_value=datetime.datetime(2021, 2, 11, 14, 13, 45))
        
    response = main(flask_request)

    assert response == mock_badge
