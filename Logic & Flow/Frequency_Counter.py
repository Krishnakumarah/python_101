def frequency_counter(data_list):
    # Write code here
    counts = {}
    for item in data_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts