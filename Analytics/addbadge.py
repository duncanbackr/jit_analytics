from datetime import datetime
from Analytics.delayscores import create_delay_scores_unscaled

def add_badge(total_comments, top_fan_cutoff, delays):
    '''Returns badge'''
    
    delay1, delay2, delay3 = delays
        
    if total_comments == 1:
        return 'newFan'                   
    elif delay3 >= 30 and delay1 < 14:
        return 'reEngageFan'
    elif total_comments > top_fan_cutoff:
        return 'topFan'
    elif delay3 < 7:
        return 'trendingFan'
    else:
        return None

    
