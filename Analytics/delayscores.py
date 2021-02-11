from datetime import datetime

def create_delay_scores(last_comment, sec_comment, time_now):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''

    delay1 = (time_now - last_comment).days 

    if sec_comment:
        delay2 = (last_comment - sec_comment).days
        delay3 = (time_now - sec_comment).days
        return [delay1, delay2, delay3]

    else:
        return [delay1, None, None]