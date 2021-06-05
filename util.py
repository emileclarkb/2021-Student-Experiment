# mean of a n-tuple
def tmean(data):
    sum = 0
    i = 0
    while i < len(data):
        sum += float(data[i])
        i += 1

    return sum/i

# minimum value in a n-tuple
def tmin(data):
    min = float(data[0])
    for i in data:
        f = float(i)
        if f < min:
            min = f
    return min

# maximum value in a n-tuple
def tmax(data):
    max = float(data[0])
    for i in data:
        f = float(i)
        if f > max:
            max = f
    return max
