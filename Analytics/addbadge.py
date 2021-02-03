from datetime import datetime, timezone
from Analytics.delayscores import create_delay_scores

def add_badge(total_comments, top_fan_cutoff, timestamp, sec_comment, max_date):
    '''takes in paramters and returns badge'''
    
    delay1 = create_delay_scores(timestamp, sec_comment, max_date)[0]
    delay2 = create_delay_scores(timestamp, sec_comment, max_date)[1]
    delay3 = create_delay_scores(timestamp, sec_comment, max_date)[2]
        
    if total_comments == 1:
        return 'new_fan'                   
    elif delay3 >= 30 and delay1 < 14:
        return 're-engaged Fan'
    elif total_comments > top_fan_cutoff:
        return 'top_fan'
    elif delay3 < 7:
        return 'trending_fan'
    else:
        return 'None'

    return badge 