import pytest
import Analytics, Filter, Formating, Query, Sort
from main import main
from Tests.test_integration.fixtures import Flask_Request
from Tests.test_integration.raw_data_comments import raw_data_comments
from Tests.test_integration.raw_data_fans import raw_data_f
from Tests.test_integration.raw_data_filter import raw_data_filter_badge


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
    video_title_list = []
    for videoid, video_title in [('365z', 'My Girl | The Temptations | Matt Mulholland Cover'), ('366z', 'And So It Goes by Billy Joel | Matt Mulholland & Chris Bill Cover')]:
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

####assert for comments correctly classified in a list###

# def test_comment_class_filter(mocker):
#     flask_request = Flask_Request({'okta_id':'00u1mjatc3FRbFhUr4x7', 'resource':'comments', 'engagement_class_id':2.0})
#     mocker.patch('Query.latest_comments',
#         return_value=raw_data_comments)
#     response = main(flask_request)
    #assert response == {}


def test_sort(mocker):
    flask_request = Flask_Request({'okta_id':'00u10v74k6FsEfLFP4x7', 'resource':'comments', 'order':'timestamp'})
    mocker.patch('Query.latest_comments',
        return_value=raw_data_comments)
    response = main(flask_request)
    assert response[1]['commentDatePosted'] > response[2]['commentDatePosted'] 