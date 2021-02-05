from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scalescores import delay1_score, delay2_score, delay3_score, comment_score, reply_score, response_score

def add_retain_score(total_comments, top_fan_cutoff, total_responses, total_replies, badge, delays):
    '''takes in parameters and returns retention score'''

    delay1, delay2, delay3 = delays
    
    if badge == 'New Fan':
        return comment_score(total_comments, top_fan_cutoff) - response_score(total_responses) + 1/delay1_score(delay1) + delay3_score(delay3) - 1 + reply_score(total_replies)
    elif badge == 're-engaged Fan':
        return comment_score(total_comments, top_fan_cutoff) - response_score(total_responses) + 1/delay1_score(delay1) + delay3_score(delay3) + 2 + reply_score(total_replies)
    else:
        return comment_score(total_comments, top_fan_cutoff) - response_score(total_responses) + delay3_score(delay3) + reply_score(total_replies)

