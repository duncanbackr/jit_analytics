from Sort.sortdata import sort_growth_score, sort_retain_score, sort_balanced_score, sort_timestamp, sort_badge_score

def backr_sort(proccessed_comments, param = None):
    '''takes in param and sorts by 'timestamp', 'balanced', 'growth', 'retention'
    default is the balanced score; can take param = None which returns the deault'''
    
    if param == 'growth':
        return sort_growth_score(proccessed_comments)
    elif param == 'retain':
        return sort_retain_score(proccessed_comments)
    elif param == 'timestamp':
        return sort_timestamp(proccessed_comments)
    elif param == 'balanced':
        return sort_balanced_score(proccessed_comments)
    elif param == 'badge':
        return sort_badge_score(proccessed_comments)
    else: 
        return sort_balanced_score(proccessed_comments)

    