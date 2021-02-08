
def from_list(proccessed_comments, param = 'balanced'):
    '''takes in param and sorts by 'timestamp', 'balanced', 'growth', 'retention'
    default is the balanced score; can take param = None which returns the default'''
    
    reverse_dict ={'growth':False, 'retention':True, 'timestamp':False, 'badge_score':True, 'balanced':True}
    
    return sorted(proccessed_comments, key=lambda k : k[param], reverse = reverse_dict[param]) 

