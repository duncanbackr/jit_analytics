from Tests.test_unpack.fixtures import raw_row, raw_rows, unpacked_rows
import datetime
from Analytics.preparedict import unpack

def test_unpack(raw_row):

    final_unpacked_row = {
        'account_title': 'H D',
        'archived': False,
        'comment_id': 10270,
        'content': "Hello it's 10:44am",
        'down_vote': None,
        'parent_youtube_comment_id': None,
        'responses': 5,
        'sec_comment': datetime.datetime(2020, 9, 18, 21, 22, 48),
        'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJzgJr8LM_13j_9prEtQ2YsJoBF-nBSUtoP9Jw=s48-c-k-c0xffffffff-no-rj-mo',
        'timestamp': datetime.datetime(2020, 9, 21, 14, 44, 50),
        'total_comments': 6,
        'total_replies': 0,
        'up_vote': None,
        'videoId': 211,
        'video_title': 'Blank video number 1',
        'video_thumbnail': 'sample_video_url',
        'note': None,
        'youtube_fan_id': 5491,
    }
    unpacked_row = unpack(raw_row)

    for key in final_unpacked_row.keys():
        assert final_unpacked_row[key] == unpacked_row[key]

def test_unpack_list(raw_rows, unpacked_rows):
    final = []
    for row in raw_rows:
        final.append(unpack(row))
    
    assert final == unpacked_rows