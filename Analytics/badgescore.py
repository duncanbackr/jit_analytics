from datetime import datetime, timezone
from Analytics.delayscores import create_delay_scores
from Analytics.scalescores import delay1_score, delay2_score, delay3_score, comment_score, reply_score, response_score

def add_fan_score(total_comments, top_fan_cutoff, total_responses, timestamp, sec_comment, max_date, badge):
    '''takes in parameters and outputs badge score'''
    
    delay1 = create_delay_scores(timestamp, sec_comment, max_date)[0]
    delay2 = create_delay_scores(timestamp, sec_comment, max_date)[1]
    delay3 = create_delay_scores(timestamp, sec_comment, max_date)[2]

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