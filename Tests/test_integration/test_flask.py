import pytest
import datetime
import Analytics, Filter, Formating, Query, Sort
from main import main
from Tests.test_integration.fixtures import Flask_Request
from Tests.test_integration.raw_data_comments import raw_data_comments
from Tests.test_integration.raw_data_fans import raw_data_f
from Tests.test_integration.raw_data_filter import raw_data_filter_badge
from Tests.test_integration.raw_data_sort import raw_data_growth, raw_data_balance, raw_data_retain, raw_data_badge
from Tests.test_integration.raw_data_class import raw_data_positive, raw_data_negative, raw_data_other, raw_data_suggest, raw_data_question

def test_home():
    flask_request = Flask_Request({})
    response = main(flask_request)
    assert response == {'error': 'must include an okta id'}

def test_fans(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'fans'})

    # mocker.patch('Analytics.datetime_now',
    #     return_value=datetime.datetime(2023,2,9))

    mocker.patch('Query.db.latest_comments',
        return_value=raw_data_f)

    response = main(flask_request)
    assert response == raw_data_f

def test_topfan_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'badge':'topFan'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    response = main(flask_request)
    assert response == raw_data_filter_badge

def test_archive_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00uw0rxwf7dgiIs3w4x6', 'resource':'comments', 'archived':True})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    response = main(flask_request)
    assert response == []

def test_video_filter(mocker):
    for videoid, video_title in [('365z', 'My Girl | The Temptations | Matt Mulholland Cover')]:
        flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'videoId':videoid})
        mocker.patch('Query.latest_comments',
            return_value=raw_data_comments)
        response = main(flask_request)

        for row in response:
            assert row['videoTitle'] == video_title

def test_multiple_video_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'videoId':'365z366z'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    response = main(flask_request)
    video_title_list = ['My Girl | The Temptations | Matt Mulholland Cover', 'And So It Goes by Billy Joel | Matt Mulholland & Chris Bill Cover']

    for row in response:
        assert row['videoTitle'] in video_title_list

def test_all_badges_filter(mocker):
    for badge in ['newFan', 'trendingFan', 'topFan', 'reEngageFan']:
        flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'badge':badge})
        mocker.patch('Query.latest_comments',
            return_value=raw_data_comments)
        response = main(flask_request)

        for row in response:
            assert row['badge'] == badge

def test_all_badges_fans_filter(mocker):
    for badge in ['newFan', 'trendingFan', 'topFan', 'reEngageFan']:
        flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'fans', 'badge':badge})
        mocker.patch('Query.latest_comments',
            return_value=raw_data_comments)
        response = main(flask_request)

        for row in response:
            assert row['badge'] == badge

def test_positive_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Positive'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
         return_value=raw_data_positive)
    assert response[0:2] == raw_data_positive[0:2]

def test_negative_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Negative'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
         return_value=raw_data_negative)
    assert response[0:2] == raw_data_negative[0:2]

def test_other_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Other'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
         return_value=raw_data_other)
    assert response[0:2] == raw_data_other[0:2]

def test_suggest_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Suggestion'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
         return_value=raw_data_suggest)
    assert response[0:2] == raw_data_suggest[0:2]

def test_question_filter(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'comment_class':'Question'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
         return_value=raw_data_question)
    assert response[0:2] == raw_data_question[0:2]

def test_sort_timestamp(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'timestamp'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    response = main(flask_request)
    assert response[1]['commentDatePosted'] > response[2]['commentDatePosted'] 

def test_sort_growth(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'growth'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
        return_value=raw_data_growth)
    assert response[0:1] == raw_data_growth[0:1]
    assert response[5:6] == raw_data_growth[5:6]

def test_sort_balanced(mocker):
    flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'order':'balanced'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
        return_value=raw_data_balance)
    assert response[0:1] == raw_data_balance[0:1]
    assert response[5:6] == raw_data_balance[5:6]

def test_sort_retain(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'retention'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
        return_value=raw_data_retain)
    assert response[0:1] == raw_data_retain[0:1]
    assert response[5:6] == raw_data_retain[5:6]

def test_sort_badge(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'badge_score'})
    response = main(flask_request)
    mocker.patch('Query.latest_comments',
        return_value=raw_data_badge)
    assert response[0:1] == raw_data_badge[0:1]
    assert response[5:6] == raw_data_badge[5:6]
