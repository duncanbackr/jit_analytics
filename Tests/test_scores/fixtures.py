import pytest
from Analytics.delayscores import create_delay_scores
from Analytics.addbadge import add_badge
from Analytics.growthscore import add_growth
from Analytics.retentionscore import add_retention
from Analytics.badgescore import  add_badge_score
from Analytics.preparedict import unpack
import Analytics
import Sort
from Filter import from_list
from datetime import datetime
from Tests.test_scores.mock_data import raw_sql_data

time_now = datetime(2021, 2, 18, 18, 32, 34)

@pytest.fixture(scope='function')
def top_fan():
    delays = create_delay_scores(datetime(2020, 9, 12, 18, 32, 34), datetime(2020, 9, 20, 18, 32, 34), time_now)
    return add_badge(3, 2, delays)

@pytest.fixture(scope='function')
def trend_fan():
    delays = create_delay_scores(datetime(2021, 1, 31, 18, 32, 34), datetime(2021, 2, 1, 18, 32, 34), time_now)
    return add_badge(2, 2, delays)

@pytest.fixture(scope='function')
def growth():
    cut_off_data = [4,2]
    final_list = Analytics.add_score(raw_sql_data, cut_off_data, time_now)
    return final_list[0][1]['growth']


@pytest.fixture(scope='function')
def retention():
    cut_off_data = [4,2]
    final_list = Analytics.add_score(raw_sql_data, cut_off_data, time_now)
    return final_list[0][1]['retention']

@pytest.fixture(scope='function')
def sort_growth():
    proccessed_comments = [{'growth':2, 'balanced':3}, {'growth':6, 'balanced':8}, {'growth':5, 'balanced':4}]
    return Sort.from_list(proccessed_comments, 'growth')

@pytest.fixture(scope='function')
def filter_badge():
    proccessed_comments = [{'growth':2, 'badge':'topFan'}, {'growth':6, 'badge':'newFan'}, {'growth':5, 'badge':'topFan'}]
    return from_list(proccessed_comments, badge = 'topFan')
