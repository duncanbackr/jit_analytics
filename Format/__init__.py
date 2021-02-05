comment_format = {
        'platformAvatar': 'thumbnail_url',
        'badge': 'badge',
        'fanID': 'youtube_fan_id',
        'authorDisplayName': 'account_title',
        'commentDatePosted': 'timestamp',
        'commentID': 'comment_id',
        'textDisplay': 'content',
        'archive': 'archived',
        'up_vote': 'up_vote',
        'down_vote': 'down_vote',
        'videoTitle': 'video_title',
        # 'Replies': [],
    }

fan_format = {
        'fanID': 'youtube_fan_id',
        'profileImage': 'thumbnail_url',
        'displayName': 'account_title',
        'note': 'note',
        'lastCommentDate': 'timestamp',
        'fanScore': 'badge_score',
        'badge': 'badge',
    }


def rename(comment, new_format):
    return {key: comment[name]
            for key, name in new_format.items()}

def comments(comments:list, reply_dict:dict):
    ''' 
        Function that re-formats comments
        
        params:
            comment = List of processed comments
            reply_dict = dictionary of replies
        returns:
            List of processed comments
    '''

    final_list = []
    for comment in comments:
        formated_comment = rename(comment, comment_format)

        replies = reply_dict.get(comment['comment_id'])
        if replies:
            formated_comment['replies'] = [rename(comment, comment_format)
                    for comment in replies]
    
        final_list.append(formated_comment)

    return final_list
        

def fans(fans:list):
    ''' 
        Function that re-formats fans keeping only first
        
        params:
            fans = List of processed comments ordered by badge score
        returns:
            List of fan objects
    '''

    fan_ids = set()
    final_list = []
    for fan in fans:
        if fan['youtube_fan_id'] not in fan_ids:
            fan_ids.add(fan['youtube_fan_id'])
            final_list.append(rename(fan, fan_format))
    
    return final_list