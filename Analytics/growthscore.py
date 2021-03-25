from datetime import datetime
from Analytics.scaler import min_max_scaler
    
def add_growth(total_comments, top_fan_cutoff, responses, badge, delays_scaled, maxs, mins):
    '''takes in parameters and outputs growth scores'''
    
    delay1_scaled, delay2_scaled, delay3_scaled = delays_scaled

    if delay1_scaled > 0:
        return 1/delay1_scaled

    else:
        return 0


    