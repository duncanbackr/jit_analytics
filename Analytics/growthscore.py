from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scaler import min_max_scaler
    
def add_growth(total_comments, top_fan_cutoff, total_responses, badge, delays, maxs, mins):
    '''takes in parameters and outputs growth scores'''

    '''
    maxs[0] - max of last date posted
    maxs[1] - max of total comments
    maxs[2] - max of total replies
    maxs[3] - max of total responses
    maxs[4] - max of second last_date posted
    '''
    
    delay1, delay2, delay3 = delays

    if badge == 'newFan':
        return 0.5 + min_max_scaler(total_responses, maxs[3], mins[3]) + delay1
    
    else:
        return min_max_scaler(total_comments, maxs[1], mins[1]) + min_max_scaler(total_responses, maxs[3], mins[3]) + \
                                delay1