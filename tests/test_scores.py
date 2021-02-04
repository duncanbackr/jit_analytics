from Tests.fixtures import unpack_row, raw_rows, unpacked_rows,new_fan, \
    top_fan, trend_fan, re_engaged_fan, other_fan
import datetime
from Analytics.preparedict import unpack
from math import nan

# ####badge tests####

def test_badge_New(new_fan):
    assert 'new_fan' ==  new_fan

def test_badge_Top(top_fan):
    assert 'top_fan' ==  top_fan

def test_badge_Trend(trend_fan):
    assert 'trending_fan' ==  trend_fan

def test_badge_Other(other_fan):
    assert 'None' ==  other_fan

def test_badge_re_engaged(re_engaged_fan):
    assert 're-engaged Fan' ==  re_engaged_fan

# ####score tests ####

# def test_score_growth(growth):
#     assert 2.35 ==  growth

# def test_score_retain(retain):
#     assert 6 ==  retain

# def test_score_badge(badge):
#     assert 2 ==  badge

# #####exeption tests#####

# def test_neg_date(neg_date):
#     assert 2 == neg_date

# def test_empty(empty):
#     assert 1.75 == empty

def test_unpack(unpack_row):
    assert unpack_row == {
        'account_title': 'H D',
        'archived': False,
        'comment_id': 10270,
        'content': "Hello it's 10:44am",
        'down_vote': None,
        'engagement_class_id': 5,
        'parent_youtube_comment_id': None,
        'responses': 5,
        'sec_comment': datetime.datetime(2020, 9, 18, 21, 22, 48),
        'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJzgJr8LM_13j_9prEtQ2YsJoBF-nBSUtoP9Jw=s48-c-k-c0xffffffff-no-rj-mo',
        'timestamp': datetime.datetime(2020, 9, 21, 14, 44, 50),
        'total_comments': 6,
        'total_replies': 0,
        'up_vote': None,
        'video_id': 211,
        'video_title': 'Blank video number 1',
        'youtube_fan_id': 5491,
    }

def test_unpack_list(raw_rows, unpacked_rows):
    final = []
    for row in raw_rows:
        final.append(unpack(row))
    
    assert final == unpacked_rows
