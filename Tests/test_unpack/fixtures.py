import pytest
from Analytics.delayscores import create_delay_scores_unscaled
from Analytics.addbadge import add_badge
from Analytics.growthscore import add_growth
from Analytics.retentionscore import add_retention
from Analytics.badgescore import  add_badge_score
from Analytics.preparedict import unpack
import Sort
from Filter import from_list
import datetime

@pytest.fixture(scope='function')

def raw_row():
    row = (10270, None, 5491, "Hello it's 10:44am", False, datetime.datetime(2020, 9, 21, 14, 44, 50), None, None, 'Blank video number 1', 211, 'sample_video_url', 6, 0, 5, datetime.datetime(2020, 9, 18, 21, 22, 48), 'H D', 'https://yt3.ggpht.com/a/AATXAJzgJr8LM_13j_9prEtQ2YsJoBF-nBSUtoP9Jw=s48-c-k-c0xffffffff-no-rj-mo', None)
    return row


@pytest.fixture(scope='function')
def raw_rows():
    return [

        (45995, None, 29614, "I'm kinda early", False, datetime.datetime(2020, 9, 1, 12, 3, 10), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, 'video_thumnail_url', 1, 0, 0, None, 'Fab_yo', 'https://yt3.ggpht.com/a/AATXAJywb5VRtA-yswjD1_gcf6stbIX1xePF-YcraLIYvA=s48-c-k-c0xffffffff-no-rj-mo', None), 
        (45931, None, 16391, 'Why do I keep seeing memes about FNAF 6 ending/connection terminated', False, datetime.datetime(2020, 9, 1, 12, 7, 45), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, 'video_thumnail_url', 7, 1, 0, datetime.datetime(2020, 11, 23, 12, 12, 24), 'Smudgy', 'https://yt3.ggpht.com/a/AATXAJxEPFIiOJHh55U6vvDvyLtm5XZQMd0ALUz9m_hHu3A=s48-c-k-c0xffffffff-no-rj-mo', None), 
        (46120, 45948, 29664, 'oooo ooooh aAHHH AAH OOOOH\n  -monke', False, datetime.datetime(2020, 9, 1, 12, 54, 59), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, 'video_thumnail_url', None, None, None, None, 'L', 'https://yt3.ggpht.com/a/AATXAJwM17GuMYlBpjlnXx8Z1MAKp09ZxiiMOpb05wXqXGk=s48-c-k-c0xffffffff-no-rj-mo', 'I am a note')
        ]

@pytest.fixture(scope='function')
def unpacked_rows():
    return [

        {
            'account_title': 'Fab_yo',
            'archived': False,
            'comment_id': 45995,
            'content': "I'm kinda early",
            'down_vote': None,
            'parent_youtube_comment_id': None,
            'responses': 0,
            'sec_comment': None,
            'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJywb5VRtA-yswjD1_gcf6stbIX1xePF-YcraLIYvA=s48-c-k-c0xffffffff-no-rj-mo',
            'timestamp': datetime.datetime(2020, 9, 1, 12, 3, 10),
            'total_comments': 1,
            'total_replies': 0,
            'note': None,
            'up_vote': None,
            'videoId': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'video_thumbnail': 'video_thumnail_url',
            'youtube_fan_id': 29614,
        },
        {
            'account_title': 'Smudgy',
            'archived': False,
            'comment_id': 45931,
            'content': 'Why do I keep seeing memes about FNAF 6 ending/connection '
                    'terminated',
            'down_vote': None,
            'parent_youtube_comment_id': None,
            'responses': 0,
            'sec_comment': datetime.datetime(2020, 11, 23, 12, 12, 24),
            'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJxEPFIiOJHh55U6vvDvyLtm5XZQMd0ALUz9m_hHu3A=s48-c-k-c0xffffffff-no-rj-mo',
            'timestamp': datetime.datetime(2020, 9, 1, 12, 7, 45),
            'total_comments': 7,
            'total_replies': 1,
            'note': None,
            'up_vote': None,
            'videoId': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'video_thumbnail': 'video_thumnail_url',
            'youtube_fan_id': 16391
        },
        {
            'account_title': 'L',
            'archived': False,
            'comment_id': 46120,
            'content': 'oooo ooooh aAHHH AAH OOOOH\n'
                    '  -monke',
            'down_vote': None,
            'parent_youtube_comment_id': 45948,
            'responses': None,
            'sec_comment': None,
            'note': 'I am a note',
            'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJwM17GuMYlBpjlnXx8Z1MAKp09ZxiiMOpb05wXqXGk=s48-c-k-c0xffffffff-no-rj-mo',
            'timestamp': datetime.datetime(2020, 9, 1, 12, 54, 59),
            'total_comments': None,
            'total_replies': None,
            'up_vote': None,
            'videoId': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'video_thumbnail': 'video_thumnail_url',
            'youtube_fan_id': 29664,
        }

    ]