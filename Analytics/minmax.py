
def min_max_scaler(value, min_value, max_value):
    scaled_value = (value - min_value)/(max_value - min_value)
    return scaled_value

