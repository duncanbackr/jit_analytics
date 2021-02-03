import math 

def unpack(row):
    '''converts row in list of lists into dictionary'''

    keys = ['comment_id', 'parent_youtube_comment_id', 'youtube_fan_id', 'content',
        'archived', 'timestamp', 'video_title', 'total_comments',
        'total_replies', 'responses', 'sec_comment', 'account_title',
        'thumbnail_url', 'max']

    comment = {keys[i]:row[i] for i in range(len(keys))} 

    return comment