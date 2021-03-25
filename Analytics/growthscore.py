from datetime import datetime
from Analytics.scaler import min_max_scaler
    
def add_growth(total_comments, top_fan_cutoff, responses, badge, delays_scaled, maxs, mins):
    '''takes in parameters and outputs growth scores'''
    
    delay1_scaled, delay2_scaled, delay3_scaled = delays_scaled

    if delay2_scaled:
        return (1 - delay2_scaled) \
            + (1 - delay1_scaled) \
            - min_max_scaler(total_comments, mins['total_comments'], maxs['total_comments']) \
            - min_max_scaler(responses, mins['responses'], maxs['responses'])
    else:
        return 2*(1 - delay1_scaled) \
            - min_max_scaler(total_comments, mins['total_comments'], maxs['total_comments']) \
            - min_max_scaler(responses, mins['responses'], maxs['responses'])

    