from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scalescores import delay1_score, delay2_score, delay3_score, comment_score, reply_score, response_score

def add_badge_score(total_comments, top_fan_cutoff, total_responses, badge, delays):
    '''takes in parameters and outputs badge score'''
    
    delay1, delay2, delay3 = delays

    if badge == 'new_fan':
        return delay1_score(delay1)

    elif badge == 'trending_fan':
        return comment_score(total_comments, top_fan_cutoff) - delay1_score(delay1)

    elif badge == 're-engaged Fan':
        return  delay2_score(delay2) - delay1_score(delay1)

    elif badge == 'top_fan':
        return comment_score(total_comments, top_fan_cutoff)

    else:
        return comment_score(total_comments, top_fan_cutoff) + (delay2_score(delay2) - delay1_score(delay1)) 