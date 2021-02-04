
def backr_sort(proccessed_comments, param = None):
    '''takes in param and sorts by 'timestamp', 'balanced', 'growth', 'retention'
    default is the balanced score; can take param = None which returns the deault'''
    
    if param == 'growth_score':
        return sorted(proccessed_comments, key=lambda k : k['growth_score']) 
    elif param == 'retain_score':
        return sorted(proccessed_comments, key=lambda k : k['retain_score'], reverse=True)
    elif param == 'timestamp':
        return sorted(proccessed_comments, key=lambda k : k['timestamp'])
    elif param == 'balanced_score':
        return sorted(proccessed_comments, key=lambda k : k['balanced_score'], reverse=True)
    elif param == 'badge_score':
        return sorted(proccessed_comments, key=lambda k : k['badge_score'], reverse=True) 
    else: 
        return sorted(proccessed_comments, key=lambda k : k['balanced_score'], reverse=True) 
