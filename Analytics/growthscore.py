from datetime import datetime
from Analytics.delayscores import create_delay_scores_scaled
from Analytics.scaler import min_max_scaler
    
def add_growth(total_comments, top_fan_cutoff, total_responses, badge, delays_scaled, maxs, mins):
    '''takes in parameters and outputs growth scores'''
    
    delay1_scaled, delay2_scaled, delay3_scaled = delays_scaled


    if badge == 'newFan':
        return min_max_scaler(total_responses, maxs['total_responses'], mins['total_responses']) + delay1_scaled
    
    elif badge == 'trendingFan':
        return min_max_scaler(total_responses, maxs['total_responses'], mins['total_responses']) + delay1_scaled
    else:
        return 0.9*min_max_scaler(total_comments, maxs['total_comments'], mins['total_comments']) + 0.5 + \
                            min_max_scaler(total_responses, maxs['total_responses'], mins['total_responses']) + delay1_scaled