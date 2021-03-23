from datetime import datetime
from Analytics.scaler import min_max_scaler
    
def add_growth(total_comments, top_fan_cutoff, responses, badge, delays_scaled, maxs, mins):
    '''takes in parameters and outputs growth scores'''
    
    delay1_scaled, delay2_scaled, delay3_scaled = delays_scaled

    if badge == 'newFan':
        return 2*delay1_scaled \
            + min_max_scaler(responses, mins['responses'], maxs['responses'])
    
    elif badge == 'trendingFan':
        return 2*delay1_scaled \
            + min_max_scaler(responses, mins['responses'], maxs['responses']) \
            + delay3_scaled
    else:
        return min_max_scaler(total_comments, mins['total_comments'], maxs['total_comments']) \
            + min_max_scaler(responses, mins['responses'], maxs['responses']) \
            + 2*delay1_scaled \
            + 0.9 