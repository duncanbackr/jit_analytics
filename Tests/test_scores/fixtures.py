import pytest
from Analytics.delayscores import create_delay_scores
from Analytics.addbadge import add_badge
from Analytics.growthscore import add_growth
from Analytics.retentionscore import add_retention
from Analytics.badgescore import  add_badge_score
from Analytics.preparedict import unpack
import Sort
from Filter import from_list
import datetime

##################badge fixtures######################

@pytest.fixture(scope='function')
def new_fan():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), None)
    return add_badge(1, 2, delays)

@pytest.fixture(scope='function')
def top_fan():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 20, 18, 32, 34))
    return add_badge(3, 2, delays)

@pytest.fixture(scope='function')
def trend_fan():
    delays = create_delay_scores(datetime.datetime(2021, 1, 31, 18, 32, 34), datetime.datetime(2021, 2, 1, 18, 32, 34))
    return add_badge(2, 2, delays)

@pytest.fixture(scope='function')
def re_engaged_fan():
    delays = create_delay_scores(datetime.datetime(2021, 1, 31, 18, 32, 34),datetime.datetime(2020, 9, 12, 18, 32, 34))
    return add_badge(2, 2, delays)

@pytest.fixture(scope='function')
def other_fan():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))
    return add_badge(2, 2, delays)


# ############score fixtures###################

@pytest.fixture(scope='function')
def growth():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 18, 18, 32, 34))
    badge = add_badge(2, 2, delays)
    return add_growth(2, 2, 0, badge, delays)


@pytest.fixture(scope='function')
def retention():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))
    badge = add_badge(3, 2, delays)
    return add_retention(3, 2, 1, 0, badge, delays)


@pytest.fixture(scope='function')
def badge():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))
    badge = add_badge(3, 2, delays)
    return  add_badge_score(3, 2, 1, badge, delays)

########sort############

# @pytest.fixture(scope='function')
# def sort_none():
#     proccessed_comments = [{'growth':2, 'balanced':3}, {'growth':6, 'balanced':8}, {'growth':5, 'balanced':4}]
#     return Sort.from_list(proccessed_comments, None)

@pytest.fixture(scope='function')
def sort_growth():
    proccessed_comments = [{'growth':2, 'balanced':3}, {'growth':6, 'balanced':8}, {'growth':5, 'balanced':4}]
    return Sort.from_list(proccessed_comments, 'growth')

########filter############

@pytest.fixture(scope='function')
def filter_badge():
    proccessed_comments = [{'growth':2, 'badge':'topFan'}, {'growth':6, 'badge':'newFan'}, {'growth':5, 'badge':'topFan'}]
    return from_list(proccessed_comments, badge = 'topFan')

@pytest.fixture(scope='function')
def filter_archived():
    proccessed_comments = [{'archived':False, 'badge':'topFan'}, {'archived':False, 'badge':'newFan'}, {'archived':True, 'badge':'topFan'}]
    return from_list(proccessed_comments, archived = True)
