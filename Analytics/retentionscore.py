from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.minmax import min_max_scaler

def remove_none(value):
    if str(value) == 'None':
        return 0

    else:
        return value

def add_retention(total_comments, top_fan_cutoff, total_responses, total_replies, badge, delays, maxs, mins):
    '''takes in parameters and returns retention score'''

    delay1, delay2, delay3 = delays
    
    if badge == 'New Fan':
        return min_max_scaler(total_comments, maxs[1], mins[1]) - min_max_scaler(total_responses, maxs[3], mins[3]) - delay1 + \
                            remove_none(delay3) - 1 + min_max_scaler(total_replies, maxs[2], mins[2])
    elif badge == 'reEngageFan':
        return min_max_scaler(total_comments, maxs[1], mins[1]) - min_max_scaler(total_responses, maxs[3], mins[3]) - delay1  + \
                                remove_none(delay3) + 2 + min_max_scaler(total_replies, maxs[2], mins[2])
    else:
        return min_max_scaler(total_comments, maxs[1], mins[1]) - min_max_scaler(total_responses, maxs[3], mins[3]) + \
                                    remove_none(delay3) +  min_max_scaler(total_replies, maxs[2], mins[2])- delay1 

