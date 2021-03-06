from Tests.test_scores.fixtures import trend_fan, top_fan, growth, retention, \
                                    sort_growth, filter_badge
import datetime
from Analytics.preparedict import unpack

def test_badge_Top(top_fan):
    assert 'topFan' ==  top_fan

def test_badge_Trend(trend_fan):
    assert None ==  trend_fan

def test_score_growth(growth):
    assert 0.7784131605810269 ==  growth

def test_score_retention(retention):
    assert 1.1 ==  retention

def test_sort_growth(sort_growth):
    assert [{'growth':6, 'balanced':8}, {'growth':5, 'balanced':4}, {'growth':2, 'balanced':3}] == sort_growth

def test_filter_badge(filter_badge):
    assert [{'growth':2, 'badge':'topFan'}, {'growth':5, 'badge':'topFan'}] == filter_badge


