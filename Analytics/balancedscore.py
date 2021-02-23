from datetime import datetime
from Analytics.delayscores import create_delay_scores_scaled
from Analytics.scaler import min_max_scaler
    
def add_balanced(total_comments, top_fan_cutoff, total_responses, total_replies, badge, delays_scaled, maxs, mins, retention, growth):
    '''takes in parameters and outputs growth scores'''
    
    delay1_scaled, delay2_scaled, delay3_scaled = delays_scaled

    if badge == 'newFan':
        return (1-growth) + retention - 0.5
    
    elif badge == 'trendingFan':
        return (1-growth) + retention - 0.25

    elif badge == 'reEngageFan':
        return retention + (1-growth) 

    elif badge == 'topFan':
        return retention + (1-growth) + 0.2
    else:
        return retention + (1-growth) - 1

    
    