
def delay_diff(time1, time2):
    '''
    takes 2 datetime objects and calculates 
    time difference in fractions of days and seconds
    '''
    delay = (time1- time2).days + ((time1 - time2).seconds)/(3600*24)

    return delay

