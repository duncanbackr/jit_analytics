from tests.fixtures import new_fan, top_fan, trend_fan, re_engaged_fan, other_fan
from tests.fixtures import growth, retain, badge
from tests.fixtures import neg_date, empty, unpack_row
from math import nan

####badge tests####

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

####score tests ####

def test_score_growth(growth):
    assert 2.35 ==  growth

def test_score_retain(retain):
    assert 6 ==  retain

def test_score_badge(badge):
    assert 2 ==  badge

#####exeption tests#####

def test_neg_date(neg_date):
    assert 2 == neg_date

def test_empty(empty):
    assert 1.75 == empty

def test_unpack(unpack_row):
    assert {'account_title': 'fan_name',
          'archived': False,
          'comment_id': 3,
          'content': 'content',
          'max': 1592585039000,
          'parent_youtube_comment_id': nan,
          'responses': 0,
          'sec_comment': nan,
          'thumbnail_url': 'url',
          'timestamp': 1589318511000,
          'total_comments': 1,
          'total_replies': 0,
          'video_title': 'video',
         'youtube_fan_id': 2} == unpack_row




