
def min_max_scaler(value, min_value, max_value):
    '''
    takes value, calculated max value (pulled from dictionary
    of maxes) and min value; and scales using min-max scaler method.
    '''
    
    try:
        return (value - min_value)/(max_value - min_value)
    except ZeroDivisionError:
        return 0

