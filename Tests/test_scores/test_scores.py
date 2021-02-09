from Tests.test_scores.fixtures import unpack_row, raw_rows, unpacked_rows,new_fan, \
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
