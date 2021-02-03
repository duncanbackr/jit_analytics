'''each function scales a different parameter used in the growth, retention and badge scores'''

def delay2_score(delay2):
    if delay2 <= 5:
        return 0.5
    elif (delay2 > 5) & (delay2 <= 14):
        return 1
    elif (delay2 > 14) & (delay2 <= 30):
        return 1.25
    elif (delay2 > 30) & (delay2 <= 60):
        return 1.75
    else:
        return 2


def delay3_score(delay3):
    if delay3 <= 5:
        return 0.5
    elif (delay3 > 5) & (delay3 <= 14):
        return 1
    elif (delay3 > 14) & (delay3 <= 30):
        return 1.25
    elif (delay3 > 30) & (delay3 <= 60):
        return 1.75
    else:
        return 2


def delay1_score(delay1):

    if delay1 <= 0:
        return 0.5
    elif (delay1 > 0) & (delay1 <= 2):
        return 1
    elif (delay1 > 2) & (delay1 <= 7):
        return 1.25
    elif (delay1 > 7) & (delay1 <= 14):
        return 1.5 
    else:
        return 2

def response_score(response):
    if isinstance(response, str):
        return 0
    else:    
        if response < 1:
            return 0.1
        elif response == 1:
            return 0.5
        elif (response > 1) & (response < 4):
            return 1
        else:
            return 2

def comment_score(comments, top_fan_cutoff):
    if comments/top_fan_cutoff <= 0.5:
        return 0.5
    elif (comments/top_fan_cutoff > 0.5) & (comments/top_fan_cutoff <= 1):
        return 1
    elif (comments/top_fan_cutoff > 1) & (comments/top_fan_cutoff < 2):
        return 1.5
    else:
        return 2

def reply_score(replies):
    if isinstance(replies, str):
        return 0
    else:
        if replies == 0:
            return 0
        elif (replies > 0) & (replies <= 2):
            return 1
        elif (replies > 2) & (replies <= 5):
            return 1.5
        else:
            return 2