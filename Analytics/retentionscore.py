from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scale import delay1_dict, delay2_dict, delay3_dict, comments_dict, \
    reply_dict, response_dict, bin_scale

def add_retention(total_comments, top_fan_cutoff, total_responses, total_replies, badge, delays):
    '''takes in parameters and returns retention score'''

    delay1, delay2, delay3 = delays
    
    x = total_comments/top_fan_cutoff
    
    if badge == 'New Fan':
        return (bin_scale(x, comments_dict) - bin_scale(total_responses, response_dict) + 1/bin_scale(delay1, delay1_dict) + 
                            bin_scale(delay3, delay3_dict) - 1 + bin_scale(total_replies, reply_dict))
    elif badge == 'reEngageFan':
        return (bin_scale(x, comments_dict) - bin_scale(total_responses, response_dict) + 1/bin_scale(delay1, delay1_dict)  + 
                                bin_scale(delay3, delay3_dict) + 2 + bin_scale(total_replies, reply_dict))
    else:
        return bin_scale(x, comments_dict) - bin_scale(total_responses, response_dict) + bin_scale(delay3, delay3_dict) + bin_scale(total_replies, reply_dict)

