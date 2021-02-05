from datetime import datetime

def create_delay_scores(timestamp, sec_comment):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''

    today = datetime.now()
    last_comment = timestamp

    delay1 = (today - last_comment).days 

    if str(sec_comment) == 'None':
        sec_last = 0
    else: 
        sec_last = sec_comment

    if sec_last != 0:
        delay2 = (last_comment - sec_last).days
    else: 
        delay2 = 8

    if sec_last != 0:
        delay3 = (today - sec_last).days
    else: 
        delay3 = 8

    return (delay1, delay2, delay3)