from datetime import datetime, timedelta
from Analytics.scaler import min_max_scaler

def create_delay_scores(last_comment, sec_comment, time_now, maxs, mins):
    '''subtracts dates in dataframe from todays date and converts 
    to # of days with logic for if the value is a nan'''
    delay1_min = (time_now - maxs['date_posted']).days + ((time_now - maxs['date_posted']).seconds)/(3600*24)
    delay1_max = (time_now - mins['date_posted']).days + ((time_now - mins['date_posted']).seconds)/(3600*24)

    delay1 = (time_now - last_comment).days + ((time_now - last_comment).seconds)/(3600*24)

    delay1_scaled = min_max_scaler(delay1, delay1_min, delay1_max)


    if sec_comment:
        delay2 = (last_comment - sec_comment).days+ ((last_comment - sec_comment).seconds)/(3600*24)
        delay2_max = (maxs['date_posted'] - mins['sec_date_posted']).days + ((maxs['date_posted'] - mins['sec_date_posted']).seconds)/(3600*24)
        delay2_min = 0
        delay2_scaled = min_max_scaler(delay2, delay2_min, delay2_max)

        delay3 = (time_now - sec_comment).days+ ((time_now - sec_comment).seconds)/(3600*24)
        delay3_min = (time_now - maxs['sec_date_posted']).days + ((time_now - maxs['sec_date_posted']).seconds)/(3600*24)
        delay3_max = (time_now - mins['sec_date_posted']).days + ((time_now - mins['sec_date_posted']).seconds)/(3600*24)
        delay3_scaled = min_max_scaler(delay3, delay3_min, delay3_max)

        return [delay1_scaled, delay2_scaled, delay3_scaled]

    else:
        return [delay1_scaled, None, None]