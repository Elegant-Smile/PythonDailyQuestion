# -*- coding:utf-8 -*-
# Author: chengbin_luo


def take_second_len(element):
    return len(element[1])


languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'), (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]

languages.sort(key=take_second_len, reverse=True)

print(languages)