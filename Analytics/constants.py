from datetime import datetime

sql_columns = [
    {'name':'comment_id', 'type':int},
    {'name':'parent_youtube_comment_id', 'type':int},
    {'name':'youtube_fan_id', 'type':int},
    {'name':'content', 'type':str},
    {'name':'archived', 'type':bool},
    {'name':'timestamp', 'type':datetime},
    {'name':'up_vote', 'type':bool},
    {'name':'down_vote', 'type':bool},
    {'name':'video_title', 'type':str},
    {'name':'video_id', 'type':int},
    {'name':'total_comments', 'type':int},
    {'name':'total_replies', 'type':int},
    {'name':'responses', 'type':int},
    {'name':'sec_comment', 'type':datetime},
    {'name':'account_title', 'type':str},
    {'name':'thumbnail_url', 'type':str},
    {'name':'engagement_class_id', 'type':int}
    ]