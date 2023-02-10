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

def moving_average(sequence, window_size=3):
    smoothed_sequence = []
    for i in range(len(sequence)):
        if i < window_size - 1:
            smoothed_sequence.append(sequence[i])
        else:
            window = sequence[i - window_size + 1: i + 1]
            smoothed_value = sum(window) / window_size
            smoothed_sequence.append(smoothed_value)
    return smoothed_sequence

def wavenumber_converter(nmList):
    wnList = []
    for nm in nmList:
        a = 10**7/785
        wn = 10**7/nm
        wnList.append(a-wn)
    return wnList