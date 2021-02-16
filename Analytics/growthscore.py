from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.minmax import min_max_scaler
from Analytics.scale import delay1_dict, delay2_dict, delay3_dict, comments_dict, \
    reply_dict, response_dict, bin_scale

    
def add_growth(total_comments, top_fan_cutoff, total_responses, badge, delays, maxs, mins):
    '''takes in parameters and outputs growth scores'''

    '''
    maxs[0] - max of last date posted
    maxs[1] - max of total comments
    maxs[2] - max of total replies
    maxs[3] - max of total responses
    maxs[4] - max of second last_date posted
    '''
    
    delay1, delay1, delay1 = delays

    if badge == 'newFan':
        return 0.5 + min_max_scaler(total_responses, maxs[3], mins[3]) + min_max_scaler(delay1, maxs[0], mins[0])
    
    else:
        return min_max_scaler(total_comments, maxs[1], mins[1]) + min_max_scaler(total_responses, maxs[3], mins[3]) + \
                                bin_scale(delay1, delay1_dict)