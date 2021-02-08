from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scale import delay1_dict, delay2_dict, delay3_dict, comments_dict, \
    reply_dict, response_dict, bin_scale

def add_badge_score(total_comments, top_fan_cutoff, total_responses, badge, delays):
    '''takes in parameters and outputs badge score'''
    
    delay1, delay2, delay3 = delays

    if badge == 'newFan':
        return bin_scale(delay1, delay1_dict)

    elif badge == 'trendingFan':
        return bin_scale(total_comments/top_fan_cutoff, comments_dict) - bin_scale(delay1, delay1_dict)

    elif badge == 'reEngageFan':
        return  bin_scale(delay2, delay2_dict) - bin_scale(delay1, delay1_dict)

    elif badge == 'topFan':
        return bin_scale(total_comments/top_fan_cutoff, comments_dict)

    else:
        return (bin_scale(total_comments/top_fan_cutoff, comments_dict) + bin_scale(delay2, delay2_dict) - 
                            bin_scale(delay1, delay1_dict))