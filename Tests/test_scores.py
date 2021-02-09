from Tests.fixtures import unpack_row, raw_rows, unpacked_rows,new_fan, \
    top_fan, trend_fan, re_engaged_fan, other_fan, growth, retention, badge, \
        sort_none, sort_growth, filter_badge, filter_archived
import datetime
from Analytics.preparedict import unpack

# ####badge tests####

def test_badge_New(new_fan):
    assert 'newFan' ==  new_fan

def test_badge_Top(top_fan):
    assert 'topFan' ==  top_fan

def test_badge_Trend(trend_fan):
    assert 'trendingFan' ==  trend_fan

def test_badge_Other(other_fan):
    assert None ==  other_fan

def test_badge_re_engaged(re_engaged_fan):
    assert 'reEngageFan' ==  re_engaged_fan

# ####score tests ####

def test_score_growth(growth):
    assert 3.6 ==  growth

def test_score_retention(retention):
    assert 3 ==  retention

def test_score_badge(badge):
    assert 1.5 ==  badge


########sort############

def test_sort_none(sort_none):
    assert [{'growth':6, 'balanced':8},{'growth':5, 'balanced':4}, {'growth':2, 'balanced':3}] == sort_none

def test_sort_growth(sort_growth):
    assert [{'growth':2, 'balanced':3}, {'growth':5, 'balanced':4}, {'growth':6, 'balanced':8}] == sort_growth


########filter############

def test_filter_badge(filter_badge):
    assert [{'growth':2, 'badge':'topFan'}, {'growth':5, 'badge':'topFan'}] == filter_badge

def test_filter_archive(filter_archived):
    assert [{'archived':True, 'badge':'topFan'}] == filter_archived


# #####exeption tests#####

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
        'note': None,
        'youtube_fan_id': 5491,
    }

def test_unpack_list(raw_rows, unpacked_rows):
    final = []
    for row in raw_rows:
        final.append(unpack(row))
    
    assert final == unpacked_rows
