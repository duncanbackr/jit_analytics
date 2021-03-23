from datetime import datetime
    
def add_balanced(total_comments, top_fan_cutoff, responses, total_replies, badge, delays_scaled, maxs, mins, retention, growth):
    '''takes in parameters and outputs growth scores'''
    
    if badge == 'newFan':
        return (1-growth) + retention - 0.5
    
    elif badge == 'trendingFan':
        return (1-growth) + retention - 0.25

    elif badge == 'reEngageFan':
        return retention + (1-growth) 

    elif badge == 'topFan':
        return retention + (1-growth) + 0.2
    else:
        return retention + (1-growth) - 0.8

    
    