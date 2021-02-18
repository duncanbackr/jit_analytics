from Tests.test_scores.fixtures import trend_fan, top_fan, growth, retention, \
                                    sort_growth, filter_archived, filter_badge
import datetime
from Analytics.preparedict import unpack

# ####badge tests####

def test_badge_Top(top_fan):
    assert 'topFan' ==  top_fan

def test_badge_Trend(trend_fan):
    assert None ==  trend_fan

def test_score_growth(growth):
    assert 1.6193477148400648 ==  growth

def test_score_retention(retention):
    assert 0.8806522851599351 ==  retention

def test_sort_growth(sort_growth):
    assert [{'growth':2, 'balanced':3}, {'growth':5, 'balanced':4}, {'growth':6, 'balanced':8}] == sort_growth

def test_filter_badge(filter_badge):
    assert [{'growth':2, 'badge':'topFan'}, {'growth':5, 'badge':'topFan'}] == filter_badge

def test_filter_archive(filter_archived):
    assert [{'archived':True, 'badge':'topFan'}] == filter_archived
