from datetime import datetime
from Analytics.delayscores import create_delay_scores

def add_badge(total_comments, top_fan_cutoff, timestamp, sec_comment):
    '''takes in paramters and returns badge'''
    
    delay1 = create_delay_scores(timestamp, sec_comment)[0]
    delay2 = create_delay_scores(timestamp, sec_comment)[1]
    delay3 = create_delay_scores(timestamp, sec_comment)[2]
        
    if total_comments == 1:
        return 'newFan'                   
    elif delay3 >= 30 and delay1 < 14:
        return 'reEngageFan'
    elif total_comments > top_fan_cutoff:
        return 'topFan'
    elif delay3 < 7:
        return 'trendingFan'
    else:
        return 'None'

    return badge 

#TODO
    #'All', 'newFan', 'topFan', 'trendingFan', 'reEngageFan', None