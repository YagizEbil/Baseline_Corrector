def min_max_normalization(data):
    max_value = max(data)
    min_value = min(data)
    normalized_data = ((data - min_value) / (max_value - min_value))
    return normalized_data

def find_closest_index(val, data):
    minErr, index = 0,0 
    for i in range(len(data)):
        dataPoint = data[i]
        err = abs(dataPoint-val)
        if err < minErr or i==0:
            minErr = err
            index = i
    return index
        