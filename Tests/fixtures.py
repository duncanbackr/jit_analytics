import pytest
from Analytics.delayscores import create_delay_scores
from Analytics.addbadge import add_badge
from Analytics.growthscore import add_growth
from Analytics.retainscore import add_retention
from Analytics.badgescore import  add_badge_score
from Analytics.preparedict import unpack
import Sort
from Filter import from_list
from math import nan
import datetime

##################badge fixtures######################

@pytest.fixture(scope='function')
def new_fan():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), None)
    return add_badge(1, 2, delays)

@pytest.fixture(scope='function')
def top_fan():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 20, 18, 32, 34))
    return add_badge(3, 2, delays)

@pytest.fixture(scope='function')
def trend_fan():
    delays = create_delay_scores(datetime.datetime(2021, 1, 31, 18, 32, 34), datetime.datetime(2021, 2, 1, 18, 32, 34))
    return add_badge(2, 2, delays)

@pytest.fixture(scope='function')
def re_engaged_fan():
    delays = create_delay_scores(datetime.datetime(2021, 1, 31, 18, 32, 34),datetime.datetime(2020, 9, 12, 18, 32, 34))
    return add_badge(2, 2, delays)

@pytest.fixture(scope='function')
def other_fan():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))
    return add_badge(2, 2, delays)


# ############score fixtures###################

@pytest.fixture(scope='function')
def growth():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 18, 18, 32, 34))
    badge = add_badge(2, 2, delays)
    return add_growth(2, 2, 0, badge, delays)


@pytest.fixture(scope='function')
def retain():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))
    badge = add_badge(3, 2, delays)
    return add_retention(3, 2, 1, 0, badge, delays)


@pytest.fixture(scope='function')
def badge():
    delays = create_delay_scores(datetime.datetime(2020, 9, 12, 18, 32, 34), datetime.datetime(2020, 9, 12, 18, 32, 34))
    badge = add_badge(3, 2, delays)
    return  add_badge_score(3, 2, 1, badge, delays)

########sort############

@pytest.fixture(scope='function')
def sort_none():
    proccessed_comments = [{'growth':2, 'balanced':3}, {'growth':6, 'balanced':8}, {'growth':5, 'balanced':4}]
    return Sort.from_list(proccessed_comments, None)

@pytest.fixture(scope='function')
def sort_growth():
    proccessed_comments = [{'growth':2, 'balanced':3}, {'growth':6, 'balanced':8}, {'growth':5, 'balanced':4}]
    return Sort.from_list(proccessed_comments, 'growth')

########filter############

@pytest.fixture(scope='function')
def filter_badge():
    proccessed_comments = [{'growth':2, 'badge':'topFan'}, {'growth':6, 'badge':'newFan'}, {'growth':5, 'badge':'topFan'}]
    return from_list(proccessed_comments, badge = 'topFan')

@pytest.fixture(scope='function')
def filter_archived():
    proccessed_comments = [{'archived':False, 'badge':'topFan'}, {'archived':False, 'badge':'newFan'}, {'archived':True, 'badge':'topFan'}]
    return from_list(proccessed_comments, archived = True)



# ################exception fixtures#################

@pytest.fixture(scope='function')
def unpack_row():
    row = (10270, None, 5491, "Hello it's 10:44am", False, datetime.datetime(2020, 9, 21, 14, 44, 50), None, None, 'Blank video number 1', 211, 6, 0, 5, datetime.datetime(2020, 9, 18, 21, 22, 48), 'H D', 'https://yt3.ggpht.com/a/AATXAJzgJr8LM_13j_9prEtQ2YsJoBF-nBSUtoP9Jw=s48-c-k-c0xffffffff-no-rj-mo', None, 5)
    return unpack(row)

@pytest.fixture(scope='function')
def raw_rows():
    return [
        (45995, None, 29614, "I'm kinda early", False, datetime.datetime(2020, 9, 1, 12, 3, 10), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, 1, 0, 0, None, 'Fab_yo', 'https://yt3.ggpht.com/a/AATXAJywb5VRtA-yswjD1_gcf6stbIX1xePF-YcraLIYvA=s48-c-k-c0xffffffff-no-rj-mo', None, 5), 
        (45931, None, 16391, 'Why do I keep seeing memes about FNAF 6 ending/connection terminated', False, datetime.datetime(2020, 9, 1, 12, 7, 45), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, 7, 1, 0, datetime.datetime(2020, 11, 23, 12, 12, 24), 'Smudgy', 'https://yt3.ggpht.com/a/AATXAJxEPFIiOJHh55U6vvDvyLtm5XZQMd0ALUz9m_hHu3A=s48-c-k-c0xffffffff-no-rj-mo', None, 5), 
        (46120, 45948, 29664, 'oooo ooooh aAHHH AAH OOOOH\n  -monke', False, datetime.datetime(2020, 9, 1, 12, 54, 59), None, None, 'Why Monki Flip Is Idiotic GENIUS', 447, None, None, None, None, 'L', 'https://yt3.ggpht.com/a/AATXAJwM17GuMYlBpjlnXx8Z1MAKp09ZxiiMOpb05wXqXGk=s48-c-k-c0xffffffff-no-rj-mo', 'I am a note', 5)
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
            'note': None,
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
            'note': None,
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
            'note': 'I am a note',
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