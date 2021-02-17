from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.minmax import min_max_scaler
from Analytics.scale import delay1_dict, delay2_dict, delay3_dict, comments_dict, \
    reply_dict, response_dict, bin_scale


def remove_none(value):
    if str(value) == 'None':
        return 0

    else:
        return value

def add_badge_score(total_comments, top_fan_cutoff, total_responses, badge, delays, maxs, mins):
    '''takes in parameters and outputs badge score'''
    
    delay1, delay2, delay3 = delays

    if badge == 'newFan':
        return delay1

    elif badge == 'trendingFan':
        return min_max_scaler(total_comments, maxs[1], mins[1]) + delay1

    elif badge == 'reEngageFan':
        return  remove_none(delay2) + delay1

    else:
        return min_max_scaler(total_comments, maxs[1], mins[1])