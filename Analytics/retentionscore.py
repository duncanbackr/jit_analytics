from datetime import datetime
from Analytics.delayscores import create_delay_scores_scaled
from Analytics.scaler import min_max_scaler

def remove_none(value):
    if str(value) == 'None':
        return 0

    else:
        return value

def add_retention(total_comments, top_fan_cutoff, total_responses, total_replies, badge, delays_scaled, maxs, mins):
    '''takes in parameters and returns retention score'''

    delay1_scaled, delay2_scaled, delay3_scaled = delays_scaled
    
    if badge == 'New Fan':
        return min_max_scaler(total_comments, maxs['total_comments'], mins['total_comments']) - min_max_scaler(total_responses, maxs['total_responses'], mins['total_responses']) - delay1_scaled + \
                            remove_none(delay3_scaled) - 1 + min_max_scaler(total_replies, maxs['total_replies'], mins['total_replies'])
    elif badge == 'reEngageFan':
        return min_max_scaler(total_comments, maxs['total_comments'], mins['total_comments']) - min_max_scaler(total_responses, maxs['total_responses'], mins['total_responses']) - delay1_scaled  + \
                                remove_none(delay3_scaled) + 2 + min_max_scaler(total_replies, maxs['total_replies'], mins['total_replies'])
    else:
        return min_max_scaler(total_comments, maxs['total_comments'], mins['total_comments']) - min_max_scaler(total_responses, maxs['total_responses'], mins['total_responses']) + \
                                    remove_none(delay3_scaled) +  min_max_scaler(total_replies, maxs['total_replies'], mins['total_replies'])- delay1_scaled

