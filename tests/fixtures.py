import pytest
from Analytics.addbadge import add_badge
from Analytics.growthscore import add_growth_score
from Analytics.retainscore import add_retain_score
from Analytics.badgescore import add_fan_score
from Analytics.preparedict import unpack
from math import nan
import datetime

##################badge fixtures######################

@pytest.fixture(scope='function')
def new_fan():
    return add_badge(1, 2, datetime.datetime(2020, 9, 12, 18, 32, 34), None)

@pytest.fixture(scope='function')
def top_fan():
    return add_badge(3, 2, datetime.datetime(2020, 9, 12, 18, 32, 34), None)

@pytest.fixture(scope='function')
def trend_fan():
    return add_badge(2, 2, datetime.datetime(2021, 1, 31, 18, 32, 34), datetime.datetime(2021, 2, 1, 18, 32, 34))

@pytest.fixture(scope='function')
def re_engaged_fan():
    return add_badge(2, 2, datetime.datetime(2021, 1, 31, 18, 32, 34),datetime.datetime(2020, 9, 12, 18, 32, 34))

@pytest.fixture(scope='function')
def other_fan():
    return add_badge(2, 2, datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))


# ############score fixtures###################

@pytest.fixture(scope='function')
def growth():
    badge = add_badge(2, 2, datetime.datetime(2020, 9, 12, 18, 32, 34),None)
    return add_growth_score(2, 2, 0, datetime.datetime(2020, 9, 12, 18, 32, 34),None, badge )


@pytest.fixture(scope='function')
def retain():
    badge = add_badge(3, 2, datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))
    return add_retain_score(3, 2, 1, 0, datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34), badge )


# @pytest.fixture(scope='function')
# def badge():
#     badge = add_badge(6, 3, 1592239439000,1591375439000 )
#     return add_fan_score(6, 3, 0, 1592239439000,1591375439000, badge)

# ################exception fixtures#################

# @pytest.fixture(scope='function')
# def neg_date():
#     badge = add_badge(6, 3, -1592239439000,1591375439000)
#     return add_fan_score(6, 3, 0, -1592239439000,1591375439000, badge)


# @pytest.fixture(scope='function')
# def empty():
#     badge = add_badge(nan, 2, 1592239439000, nan)
#     return add_fan_score(nan, nan, nan, 1592239439000, nan, badge)

@pytest.fixture(scope='function')
def unpack_row():
    row = (10270, None, 5491, "Hello it's 10:44am", False, datetime.datetime(2020, 9, 21, 14, 44, 50), None, None, 'Blank video number 1', 211, 6, 0, 5, datetime.datetime(2020, 9, 18, 21, 22, 48), 'H D', 'https://yt3.ggpht.com/a/AATXAJzgJr8LM_13j_9prEtQ2YsJoBF-nBSUtoP9Jw=s48-c-k-c0xffffffff-no-rj-mo', 5)
    return unpack(row)

@pytest.fixture(scope='function')
def raw_rows():
    return [
        (45995, None, 29614, "I'm kinda early", False, datetime.datetime(2020, 9, 1, 12, 3, 10), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, 1, 0, 0, None, 'Fab_yo', 'https://yt3.ggpht.com/a/AATXAJywb5VRtA-yswjD1_gcf6stbIX1xePF-YcraLIYvA=s48-c-k-c0xffffffff-no-rj-mo', 5), 
        (45931, None, 16391, 'Why do I keep seeing memes about FNAF 6 ending/connection terminated', False, datetime.datetime(2020, 9, 1, 12, 7, 45), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, 7, 1, 0, datetime.datetime(2020, 11, 23, 12, 12, 24), 'Smudgy', 'https://yt3.ggpht.com/a/AATXAJxEPFIiOJHh55U6vvDvyLtm5XZQMd0ALUz9m_hHu3A=s48-c-k-c0xffffffff-no-rj-mo', 5), 
        (46120, 45948, 29664, 'oooo ooooh aAHHH AAH OOOOH\n  -monke', False, datetime.datetime(2020, 9, 1, 12, 54, 59), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, None, None, None, None, 'L', 'https://yt3.ggpht.com/a/AATXAJwM17GuMYlBpjlnXx8Z1MAKp09ZxiiMOpb05wXqXGk=s48-c-k-c0xffffffff-no-rj-mo', 5)
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
            'engagement_class_id': 5,
            'parent_youtube_comment_id': None,
            'responses': 0,
            'sec_comment': None,
            'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJywb5VRtA-yswjD1_gcf6stbIX1xePF-YcraLIYvA=s48-c-k-c0xffffffff-no-rj-mo',
            'timestamp': datetime.datetime(2020, 9, 1, 12, 3, 10),
            'total_comments': 1,
            'total_replies': 0,
            'up_vote': None,
            'video_id': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'youtube_fan_id': 29614,
        },
        {
            'account_title': 'Smudgy',
            'archived': False,
            'comment_id': 45931,
            'content': 'Why do I keep seeing memes about FNAF 6 ending/connection '
                    'terminated',
            'down_vote': None,
            'engagement_class_id': 5,
            'parent_youtube_comment_id': None,
            'responses': 0,
            'sec_comment': datetime.datetime(2020, 11, 23, 12, 12, 24),
            'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJxEPFIiOJHh55U6vvDvyLtm5XZQMd0ALUz9m_hHu3A=s48-c-k-c0xffffffff-no-rj-mo',
            'timestamp': datetime.datetime(2020, 9, 1, 12, 7, 45),
            'total_comments': 7,
            'total_replies': 1,
            'up_vote': None,
            'video_id': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'youtube_fan_id': 16391
        },
        {
            'account_title': 'L',
            'archived': False,
            'comment_id': 46120,
            'content': 'oooo ooooh aAHHH AAH OOOOH\n'
                    '  -monke',
            'down_vote': None,
            'engagement_class_id': 5,
            'parent_youtube_comment_id': 45948,
            'responses': None,
            'sec_comment': None,
            'thumbnail_url': 'https://yt3.ggpht.com/a/AATXAJwM17GuMYlBpjlnXx8Z1MAKp09ZxiiMOpb05wXqXGk=s48-c-k-c0xffffffff-no-rj-mo',
            'timestamp': datetime.datetime(2020, 9, 1, 12, 54, 59),
            'total_comments': None,
            'total_replies': None,
            'up_vote': None,
            'video_id': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'youtube_fan_id': 29664,
        }

    ]