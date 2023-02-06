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
