from datetime import datetime
from Analytics.scaler import min_max_scaler

def add_badge_score(total_comments, top_fan_cutoff, responses, badge, delays, maxs, mins):
    '''takes in parameters and outputs badge score'''
    
    delay1_scaled, delay2_scaled, delay3_scaled = delays

    if badge == 'newFan':
        return -delay1_scaled

    elif badge == 'trendingFan':
        return min_max_scaler(total_comments, mins['total_comments'], maxs['total_comments']) - delay1_scaled


    elif (badge == 'reEngageFan') and (delay2_scaled):
        return  delay2_scaled - delay1_scaled

    else:
        return min_max_scaler(total_comments, mins['total_comments'], maxs['total_comments'])