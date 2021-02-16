from datetime import datetime, timedelta

def create_delay_scores(last_comment, sec_comment, time_now):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''
    delay_1_max = time_now - max_time


    delay1 = (time_now - last_comment).days + ((time_now - last_comment).seconds)/(3600*24)

    if sec_comment:
        delay2 = (last_comment - sec_comment).days+ ((last_comment - sec_comment).seconds)/(3600*24)
        delay3 = (time_now - sec_comment).days+ ((time_now - sec_comment).seconds)/(3600*24)
        return [delay1, delay2, delay3]

    else:
        return [delay1, None, None]