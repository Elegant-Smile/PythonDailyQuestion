'''
列表 languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'), (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]，
请进行排序，实现效果：
[(4, 'Erlang'), (5, 'Kotlin'), (6, 'Python'), (3, 'Swift'), (2, 'Ruby'), (1, 'Go')]
'''
languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'), (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]

a = sorted(languages,key=lambda x:len(x[1]),reverse=True)

print(a)