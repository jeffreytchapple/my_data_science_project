"""
    Generates a frequency table from the given data.

    Parameters:
    data (list): A list of elements to analyze.

    Returns:
    dict: A dictionary with elements as keys and their frequencies as values.
    """

def frequency_table(data):
    freq_table = {}
    
    for item in data:
        if item in freq_table:
            freq_table[item] += 1
        else:
            freq_table[item] = 1
    return freq_table

"""
a version of this function for passing in multiple parameters

"""
def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    
    return frequency_table