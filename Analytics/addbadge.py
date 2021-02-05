from datetime import datetime
from Analytics.delayscores import create_delay_scores

def add_badge(total_comments, top_fan_cutoff, delays):
    '''Returns badge'''
    
    delay1, delay2, delay3 = delays
        
    if total_comments == 1:
        return 'new_fan' 

    elif delay3 >= 30 and delay1 < 14:
        return 're-engaged Fan'
    
    elif total_comments > top_fan_cutoff:
        return 'top_fan'
    
    elif delay3 < 7:
        return 'trending_fan'
    
    else:
        return 'None'
