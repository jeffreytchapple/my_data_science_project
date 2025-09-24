def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a + b

def add_10(a):
    if not isinstance(a, (int, float)):
        raise ValueError("Argument must be a number.")
    return add(a, 10)

def square(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    return x * x

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length


def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)
    
# avg_price = mean(apps_data, 4)