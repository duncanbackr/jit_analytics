from Tests.test_general.fixtures import unpack_row, raw_rows, unpacked_rows,new_fan, \
    top_fan, trend_fan, re_engaged_fan, other_fan, growth, retention, badge, \
        sort_none, sort_growth, filter_badge, filter_archived
import datetime
from Analytics.preparedict import unpack

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
