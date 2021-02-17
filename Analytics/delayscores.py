from datetime import datetime, timedelta
from Analytics.scaler import min_max_scaler

def create_delay_scores_scaled(last_comment, sec_comment, time_now, delay_max, delay_min):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''
    delay1 = (time_now - last_comment).days + ((time_now - last_comment).seconds)/(3600*24)
    delay1_scaled = min_max_scaler(delay1, delay_min["delay1"], delay_max["delay1"])


    if sec_comment:
        delay2 = (last_comment - sec_comment).days+ ((last_comment - sec_comment).seconds)/(3600*24)
        delay2_scaled = min_max_scaler(delay2, delay_min["delay2"], delay_max["delay2"])

        delay3 = (time_now - sec_comment).days+ ((time_now - sec_comment).seconds)/(3600*24)
        delay3_scaled = min_max_scaler(delay3, delay_min["delay3"], delay_max["delay3"])

        return [delay1_scaled, delay2_scaled, delay3_scaled]

    else:
        return [delay1_scaled, None, None]

def create_delay_scores_unscaled(last_comment, sec_comment, time_now):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''
    delay1 = (time_now - last_comment).days + ((time_now - last_comment).seconds)/(3600*24)

    if sec_comment:
        delay2 = (last_comment - sec_comment).days+ ((last_comment - sec_comment).seconds)/(3600*24)
        delay3 = (time_now - sec_comment).days+ ((time_now - sec_comment).seconds)/(3600*24)

        return [delay1, delay2, delay3]

    else:
        return [delay1, None, None]



