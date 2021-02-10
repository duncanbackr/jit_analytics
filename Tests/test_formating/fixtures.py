import pytest
import datetime

@pytest.fixture(scope='function')
def proccessed_comments_1():
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
            'videoId': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'youtube_fan_id': 29614,
            'badge': 'topFan',
        },
        {
            'account_title': 'Smudgy',
            'archived': False,
            'comment_id': 45948,
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
            'videoId': 447,
            'video_title': 'Why Monki Flip Is Idiotic GENIUS',
            'youtube_fan_id': 16391,
            'badge': 'newFan'
        }
    ]

@pytest.fixture(scope='function')
def formated_comments_1():
    return [
        {'archive': False,
        'authorDisplayName': 'Fab_yo',
        'badge': 'topFan',
        'commentDatePosted': datetime.datetime(2020, 9, 1, 12, 3, 10),
        'commentID': 45995,
        'down_vote': None,
        'fanID': 29614,
        'platformAvatar': 'https://yt3.ggpht.com/a/AATXAJywb5VRtA-yswjD1_gcf6stbIX1xePF-YcraLIYvA=s48-c-k-c0xffffffff-no-rj-mo',
        'textDisplay': "I'm kinda early",
        'up_vote': None,
        'videoTitle': 'Why Monki Flip Is Idiotic GENIUS'},
        {'archive': False,
        'authorDisplayName': 'Smudgy',
        'badge': 'newFan',
        'commentDatePosted': datetime.datetime(2020, 9, 1, 12, 7, 45),
        'commentID': 45948,
        'down_vote': None,
        'fanID': 16391,
        'platformAvatar': 'https://yt3.ggpht.com/a/AATXAJxEPFIiOJHh55U6vvDvyLtm5XZQMd0ALUz9m_hHu3A=s48-c-k-c0xffffffff-no-rj-mo',
        'textDisplay': 'Why do I keep seeing memes about FNAF 6 ending/connection '
                        'terminated',
        'up_vote': None,
        'videoTitle': 'Why Monki Flip Is Idiotic GENIUS'}
        ]


@pytest.fixture(scope='function')
def processed_reply_1():
    return {
            45948: [{
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
                    'videoId': 447,
                    'video_title': 'Why Monki Flip Is Idiotic GENIUS',
                    'youtube_fan_id': 29664,
                    'badge': 'topFan'
                }]
    }

@pytest.fixture(scope='function')
def formated_comments_1_with_reply():
    return [
        {'archive': False,
        'authorDisplayName': 'Fab_yo',
        'badge': 'topFan',
        'commentDatePosted': datetime.datetime(2020, 9, 1, 12, 3, 10),
        'commentID': 45995,
        'down_vote': None,
        'fanID': 29614,
        'platformAvatar': 'https://yt3.ggpht.com/a/AATXAJywb5VRtA-yswjD1_gcf6stbIX1xePF-YcraLIYvA=s48-c-k-c0xffffffff-no-rj-mo',
        'textDisplay': "I'm kinda early",
        'up_vote': None,
        'videoTitle': 'Why Monki Flip Is Idiotic GENIUS'},
        {'archive': False,
        'authorDisplayName': 'Smudgy',
        'badge': 'newFan',
        'commentDatePosted': datetime.datetime(2020, 9, 1, 12, 7, 45),
        'commentID': 45948,
        'down_vote': None,
        'fanID': 16391,
        'platformAvatar': 'https://yt3.ggpht.com/a/AATXAJxEPFIiOJHh55U6vvDvyLtm5XZQMd0ALUz9m_hHu3A=s48-c-k-c0xffffffff-no-rj-mo',
        'textDisplay': 'Why do I keep seeing memes about FNAF 6 ending/connection '
                        'terminated',
        'up_vote': None,
        'videoTitle': 'Why Monki Flip Is Idiotic GENIUS',
        'replies': [
                {'archive': False,
                'authorDisplayName': 'L',
                'commentDatePosted': datetime.datetime(2020, 9, 1, 12, 54, 59),
                'commentID': 46120,
                'down_vote': None,
                'fanID': 29664,
                'platformAvatar': 'https://yt3.ggpht.com/a/AATXAJwM17GuMYlBpjlnXx8Z1MAKp09ZxiiMOpb05wXqXGk=s48-c-k-c0xffffffff-no-rj-mo',
                'textDisplay': 'oooo ooooh aAHHH AAH OOOOH\n'
                                '  -monke',
                'up_vote': None,
                'videoTitle': 'Why Monki Flip Is Idiotic GENIUS'}
            ]
        }
    ]
