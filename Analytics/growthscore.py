from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scale import delay1_dict, delay2_dict, delay3_dict, comments_dict, \
    reply_dict, response_dict, bin_scale
    
def add_growth(total_comments, top_fan_cutoff, total_responses, badge, delays):
    '''takes in parameters and outputs growth scores'''
    
    delay1, delay1, delay1 = delays

    if badge == 'newFan':
        return 0.5 + bin_scale(total_responses, response_dict) + bin_scale(delay1, delay1_dict)
    
    else:
        return (bin_scale(total_comments/top_fan_cutoff, comments_dict) + bin_scale(total_responses, response_dict) + 
                                bin_scale(delay1, delay1_dict))