def half(array):
    for i in set(array):
        if array.count(i) > len(array):
            return i 
    return 0
