from datetime import datetime

def create_delay_scores(last_comment, sec_comment):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''

    today = datetime.utcnow()

    delay1 = (today - last_comment).days 

    if sec_comment:
        delay2 = (last_comment - sec_comment).days
        delay3 = (today - sec_comment).days
        return [delay1, delay2, delay3]

    else:
        return [delay1, None, None]