
def sort_growth_score(proccessed_comments):
    return sorted(proccessed_comments, key=lambda k : k['growth_score']) 

def sort_retain_score(proccessed_comments):
    return sorted(proccessed_comments, key=lambda k : k['retain_score'], reverse=True) 

def sort_balanced_score(proccessed_comments):
    return sorted(proccessed_comments, key=lambda k : k['balanced_score'], reverse=True) 

def sort_badge_score(proccessed_comments):
    return sorted(proccessed_comments, key=lambda k : k['badge_score'], reverse=True) 

def sort_timestamp(proccessed_comments):
    return sorted(proccessed_comments, key=lambda k : k['timestamp']) 



