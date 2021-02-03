from datetime import datetime, timezone

def create_delay_scores(timestamp, sec_comment, max_date):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''

    today = datetime.fromtimestamp(max_date/1000)
    last_comment = datetime.fromtimestamp(timestamp/1000)

    delay1 = (today - last_comment).days 

    if str(sec_comment) == 'nan':
        sec_last = 0
    else: 
        sec_last = datetime.fromtimestamp(sec_comment/1000)

    if sec_last != 0:
        delay2 = (last_comment - sec_last).days
    else: 
        delay2 = 8

    if sec_last != 0:
        delay3 = (today - sec_last).days
    else: 
        delay3 = 8

    return (delay1, delay2, delay3)