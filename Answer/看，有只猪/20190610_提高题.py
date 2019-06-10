def find(string):
    counter = {}
    for index, v in enumerate(string):
        if v not in counter:
            counter[v] = {
                'index': index,
                'count': 1
            }
        else:
            counter[v]['count'] += 1

    sorted_counter = sorted(counter.items(), key=lambda v: (v[1]['count'], v[1]['index']))
    return sorted_counter[0]


if __name__ == '__main__':
    find('google')
