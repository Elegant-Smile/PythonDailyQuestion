def one(array):
    count = 0
    for i in array:
        count += i.count(1)
    return count
