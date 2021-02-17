
def min_delay(time_now, max_value):
    '''
    takes a datetime object and calculates 
    delay for max dates
    '''
    delay_min = (time_now - max_value).days + ((time_now - max_value).seconds)/(3600*24)

    return delay_min

def max_delay(time_now, min_value):
    '''
    takes a datetime object and calculates 
    delay for min dates
    '''
    delay_max = (time_now - min_value).days + ((time_now - min_value).seconds)/(3600*24)

    return delay_max
