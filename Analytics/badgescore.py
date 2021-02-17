from datetime import datetime
from Analytics.delayscores import create_delay_scores
from Analytics.scale import delay1_dict, delay2_dict, delay3_dict, comments_dict, \
    reply_dict, response_dict, bin_scale

def add_badge_score(total_comments, top_fan_cutoff, total_responses, badge, delays):
    '''takes in parameters and outputs badge score'''
    
    delay1, delay2, delay3 = delays

    if badge == 'newFan':
        return 1/delay1

    elif badge == 'trendingFan':
        return total_comments/top_fan_cutoff + (1/delay1)

    elif badge == 'reEngageFan':
        return  bin_scale(delay2, delay2_dict) - 1/bin_scale(delay1, delay1_dict)

    else:
        return total_comments/top_fan_cutoff