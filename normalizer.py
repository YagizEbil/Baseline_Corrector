def min_max_normalization(data):
    max_value = max(data)
    min_value = min(data)
    normalized_data = ((data - min_value) / (max_value - min_value))
    return normalized_data