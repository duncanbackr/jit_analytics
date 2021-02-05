from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scalescores import delay1_score, delay2_score, delay3_score, comment_score, reply_score, response_score

def add_growth(total_comments, top_fan_cutoff, total_responses, badge, delays):
    '''takes in parameters and outputs growth scores'''
    
    delay1, delay1, delay1 = delays

    if badge == 'newFan':
        return 0.5 + response_score(total_responses) + delay1_score(delay1)
    
    else:
        return comment_score(total_comments, top_fan_cutoff) + response_score(total_responses) + delay1_score(delay1)