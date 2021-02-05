from datetime import datetime

sql_columns = [
    {
        'name':'comment_id', 
        'type':int, 
        'required': True
    },
    {
        'name':'parent_youtube_comment_id', 
        'type':int,
        'required': False
    },
    {
        'name':'youtube_fan_id', 
        'type':int, 
        'required': True
    },
    {
        'name':'content', 
        'type':str, 
        'required': True
    },
    {
        'name':'archived', 
        'type':bool, 
        'required': True
    },
    {
        'name':'timestamp', 
        'type':datetime, 
        'required': True
    },
    {
        'name':'up_vote', 
        'type':bool, 
        'required': False
    },
    {
        'name':'down_vote', 
        'type':bool, 
        'required': False
    },
    {
        'name':'video_title', 
        'type':str, 
        'required': True
    },
    {
        'name':'video_id', 
        'type':int, 
        'required': True
    },
    {
        'name':'total_comments', 
        'type':int, 
        'required': False
    },
    {
        'name':'total_replies', 
        'type':int, 
        'required': False
    },
    {
        'name':'responses', 
        'type':int, 
        'required': False
    },
    {
        'name':'sec_comment', 
        'type':datetime, 
        'required': False
    },
    {
        'name':'account_title', 
        'type':str, 
        'required': True
    },
    {
        'name':'thumbnail_url', 
        'type':str, 
        'required': False
    },
    {
        'name': 'note', 
        'type':str, 
        'required': False
    }
    {
        'name': 'engagement_class_id', 
        'type':int, 
        'required': False
    }
]