from datetime import datetime
from Analytics.scaler import min_max_scaler

def add_retention(total_comments, top_fan_cutoff, responses, total_replies, badge, delays_scaled, maxs, mins):
    '''takes in parameters and returns retention score'''

    delay1_scaled, delay2_scaled, delay3_scaled = delays_scaled

    if delay3_scaled:
        return min_max_scaler(total_comments, mins['total_comments'], maxs['total_comments']) \
            - min_max_scaler(responses, mins['responses'], maxs['responses'])

    else:
        return min_max_scaler(total_comments, mins['total_comments'], maxs['total_comments']) \
                - min_max_scaler(responses, mins['responses'], maxs['responses'])

