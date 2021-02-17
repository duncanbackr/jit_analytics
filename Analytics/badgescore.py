from datetime import datetime
from Analytics.delayscores import create_delay_scores_scaled
from Analytics.scaler import min_max_scaler

def remove_none(value):
    if str(value) == 'None':
        return 0
    else:
        return value

def add_badge_score(total_comments, top_fan_cutoff, total_responses, badge, delays, maxs, mins):
    '''takes in parameters and outputs badge score'''
    
    delay1_scaled, delay2_scaled, delay3_scaled = delays

    if badge == 'newFan':
        return -delay1_scaled

    elif badge == 'trendingFan':
        return min_max_scaler(total_comments, maxs['total_comments'], mins['total_comments']) - delay1_scaled

    elif badge == 'reEngageFan':
        return  remove_none(delay2_scaled) - delay1_scaled

    else:
        return min_max_scaler(total_comments, maxs['total_comments'], mins['total_comments'])